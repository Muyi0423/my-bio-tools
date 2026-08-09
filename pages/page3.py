import streamlit as st
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import io
import base64
from openpyxl import Workbook
from openpyxl.drawing.image import Image as OpenpyxlImage
import re

# --- 页面配置 ---
st.set_page_config(page_title="EC50 批量分析工具", layout="wide")
st.title("🧬 EC50 批量剂量-反应曲线分析工具")

# 核心算法：四参数逻辑斯蒂模型 (4PL)
def four_param_logistic(x, a, b, c, d):
    # a: 最小响应值 (Bottom)
    # d: 最大响应值 (Top)
    # c: EC50 (Inflection point)
    # b: Hill Slope
    return d + (a - d) / (1 + 10**((c - x) * b))

# ============================
# 主功能区：批量分析 (适配新模板)
# ============================

st.header("📂 批量分析 (Excel导入)")
st.info("请上传符合模板的Excel文件。每一组数据需包含两列：`xxx_Conc` (浓度) 和 `xxx_eff` (效应值)。")

uploaded_file = st.file_uploader("上传 Excel 文件 (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.success("文件上传成功！正在分析...")
        
        # 1. 自动识别列配对
        # 我们寻找以 _Conc 结尾的列，并尝试找到对应的 _eff 列
        conc_cols = [col for col in df.columns if str(col).endswith('_Conc')]
        
        if not conc_cols:
            st.error("未找到格式为 'xxx_Conc' 的浓度列，请检查表头。")
        else:
            results_data = []
            fig, axes = plt.subplots(len(conc_cols), 1, figsize=(10, 5 * len(conc_cols)))
            if len(conc_cols) == 1:
                axes = [axes] # 确保即使只有一个图也是列表

            compound_index = 0
            
            for conc_col in conc_cols:
                # 推导对应的 eff 列名 (例如 Compound_A_Conc -> Compound_A_eff)
                base_name = conc_col.replace('_Conc', '')
                eff_col = f"{base_name}_eff"
                
                if eff_col not in df.columns:
                    st.warning(f"⚠️ 警告: 找到了浓度列 '{conc_col}'，但未找到对应的效应列 '{eff_col}'，已跳过该化合物。")
                    continue
                
                # 提取数据并清洗
                data = df[[conc_col, eff_col]].dropna()
                x_data = data[conc_col].values.astype(float)
                y_data = data[eff_col].values.astype(float)
                
                # 过滤掉非正数浓度（对数坐标需要）
                valid_idx = x_data > 0
                x_data = x_data[valid_idx]
                y_data = y_data[valid_idx]

                if len(x_data) < 3:
                    st.warning(f"⚠️ {base_name} 有效数据点少于3个，无法拟合。")
                    continue

                # 2. 进行拟合
                try:
                    # 初始参数猜测: Bottom=0, Hill=1, EC50=中位数浓度, Top=100
                    p0 = [min(y_data), 1.0, np.median(x_data), max(y_data)]
                    bounds = ([0, -10, min(x_data), 0], [100, 10, max(x_data), 150]) # 限制范围防止跑飞
                    
                    popt, pcov = curve_fit(four_param_logistic, x_data, y_data, p0=p0, bounds=bounds, maxfev=10000)
                    
                    a, b, c, d = popt
                    ec50_val = c
                    
                    results_data.append({
                        "化合物名称": base_name,
                        "EC50": f"{ec50_val:.4f}",
                        "Hill Slope": f"{b:.4f}",
                        "Bottom (A)": f"{a:.2f}",
                        "Top (D)": f"{d:.2f}"
                    })
                    
                    # 3. 绘图
                    ax = axes[compound_index]
                    # 生成平滑曲线的数据点
                    x_plot = np.logspace(np.log10(min(x_data)), np.log10(max(x_data)), 100)
                    y_plot = four_param_logistic(x_plot, *popt)
                    
                    ax.semilogx(x_data, y_data, 'bo', label='实验数据') # 原始数据点
                    ax.semilogx(x_plot, y_plot, 'r-', label=f'拟合曲线 (EC50={ec50_val:.4f})') # 拟合线
                    ax.set_title(f"{base_name} Dose-Response Curve")
                    ax.set_xlabel("Concentration")
                    ax.set_ylabel("Effect (%)")
                    ax.legend()
                    ax.grid(True, which="both", ls="-", alpha=0.2)
                    
                    compound_index += 1
                    
                except Exception as e:
                    st.error(f"❌ {base_name} 拟合失败: {str(e)}")

            # 4. 展示结果
            if results_data:
                st.subheader("📊 分析结果汇总")
                result_df = pd.DataFrame(results_data)
                st.dataframe(result_df, use_container_width=True)
                
                st.subheader("📈 拟合曲线图")
                st.pyplot(fig)
                
                # 5. 下载功能
                # 合并 Excel (数据表 + 图片)
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    result_df.to_excel(writer, index=False, sheet_name='EC50_Results')
                
                output.seek(0)
                
                # 保存图表到内存以便放入 Excel (可选，这里仅提供图表下载)
                img_buf = io.BytesIO()
                fig.savefig(img_buf, format='png', bbox_inches='tight')
                img_buf.seek(0)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        label="📥 下载结果表格 (.xlsx)",
                        data=output,
                        file_name="EC50_Batch_Results.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                with col2:
                     st.download_button(
                        label="📥 下载拟合曲线图 (.png)",
                        data=img_buf,
                        file_name="EC50_Curves.png",
                        mime="image/png"
                    )

    except Exception as e:
        st.error(f"处理文件时发生错误: {e}")

else:
    st.info("👆 请在上方上传 Excel 文件开始分析。")
    
    # 提供模板下载逻辑（可选）
    st.markdown("---")
    st.caption("💡 提示：Excel表头必须严格遵循 `名称_Conc` 和 `名称_eff` 的格式，例如 `DrugA_Conc` 和 `DrugA_eff`。")