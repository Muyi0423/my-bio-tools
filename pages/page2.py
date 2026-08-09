import streamlit as st
import pandas as pd

# --- 核心逻辑函数 ---
def run_allocation_logic(live_dead_dye, antigen_list, fluorophore_db, instrument_slots):
    final_panel = {}
    
    # Step 1: 处理死活染料
    if live_dead_dye in fluorophore_db:
        dye_info = fluorophore_db[live_dead_dye]
        laser_name = dye_info["laser"]
        if laser_name in instrument_slots:
            if len(instrument_slots[laser_name]["used"]) < instrument_slots[laser_name]["capacity"]:
                instrument_slots[laser_name]["used"].append(live_dead_dye)
                final_panel["Live/Dead"] = live_dead_dye
            else:
                return None, f"错误：{laser_name} 通道已满，无法放入 {live_dead_dye}"
        else:
            return None, f"错误：找不到激光器 {laser_name}"
    else:
        return None, f"错误：数据库中未找到染料 '{live_dead_dye}'"

    # Step 2: 处理抗原列表
    priority_map = {"弱表达 (Weak)": 0, "中等 (Medium)": 1, "强表达 (Strong)": 2}
    sorted_antigens = sorted(antigen_list, key=lambda x: priority_map.get(x[1], 3))

    for antigen, strength in sorted_antigens:
        assigned = False
        candidates = []
        for name, info in fluorophore_db.items():
            if name in final_panel.values():
                continue
            rank = info["si_rank"]
            if strength == "弱表达 (Weak)" and rank >= 7:
                candidates.append((name, rank))
            elif strength == "中等 (Medium)" and rank >= 5:
                candidates.append((name, rank))
            elif strength == "强表达 (Strong)":
                candidates.append((name, rank))
        
        candidates.sort(key=lambda x: x[1], reverse=True)

        for dye_name, rank in candidates:
            dye_laser = fluorophore_db[dye_name]["laser"]
            if dye_laser in instrument_slots:
                if len(instrument_slots[dye_laser]["used"]) < instrument_slots[dye_laser]["capacity"]:
                    instrument_slots[dye_laser]["used"].append(dye_name)
                    final_panel[antigen] = dye_name
                    assigned = True
                    break
        if not assigned:
            final_panel[antigen] = "⚠️ 未找到合适染料"

    return final_panel, "成功"

# --- 辅助函数：智能识别抗原强度 ---
def auto_detect_strength(antigen_name):
    """
    根据抗原名称自动判断其表达强度。
    """
    antigen_name = antigen_name.upper()
    
    # 定义强表达抗原列表
    strong_markers = ["CD3", "CD45", "CD4", "CD8", "CD19", "CD14", "CD56", "HLA-DR"]
    # 定义弱表达抗原列表
    weak_markers = ["CD25", "CXCR5", "PD-1", "CTLA-4", "CD127", "CCR7", "CD45RA"]
    
    for marker in strong_markers:
        if marker in antigen_name:
            return "强表达 (Strong)"
    for marker in weak_markers:
        if marker in antigen_name:
            return "弱表达 (Weak)"
            
    return "中等 (Medium)"

# --- 网页界面部分 ---
st.title("🧬 流式配色智能小助手")
st.markdown("告别手动查表，一键生成最优配色方案！")

# 使用列布局来调整左右比例 (1:1)
col_config, col_result = st.columns([1, 1])

with col_config:
    st.header("⚙️ 实验配置")
    
    # 死活染料选择
    live_dead_options = ["7-AAD", "Zombie NIR", "UV395", "PI", "DAPI"]
    selected_live_dead = st.selectbox("1. 选择死活染料", live_dead_options)
    
    st.markdown("---")
    st.subheader("2. 输入你的抗原列表")
    st.caption("在左侧输入抗原名称，点击按钮后强度会自动识别。")
    
    # 创建一个13行2列的空白数据框
    default_data = {"抗原": [""] * 13, "强度": ["中等 (Medium)"] * 13}
    df = pd.DataFrame(default_data)
    
    # 使用数据编辑器
    edited_df = st.data_editor(
        df,
        num_rows="dynamic",
        column_config={
            "强度": st.column_config.SelectboxColumn(
                "强度",
                help="抗原的表达强度",
                options=["强表达 (Strong)", "中等 (Medium)", "弱表达 (Weak)"],
                required=True,
            )
        },
        hide_index=True,
        height=450,
        key="antigen_editor"
    )

with col_result:
    st.header("🎨 配色方案")
    
    if st.button('🚀 开始智能配色', type="primary", use_container_width=True):
        # --- 数据准备 ---
        FLUOROPHORE_DB = {
            "BV421": {"laser": "Violet (405)", "si_rank": 9}, "BV510": {"laser": "Violet (405)", "si_rank": 7},
            "BV605": {"laser": "Violet (405)", "si_rank": 8}, "BV650": {"laser": "Violet (405)", "si_rank": 6},
            "BV711": {"laser": "Violet (405)", "si_rank": 8}, "BV785": {"laser": "Violet (405)", "si_rank": 7},
            "FITC": {"laser": "Blue (488)", "si_rank": 5}, "PE": {"laser": "Blue (488)", "si_rank": 10},
            "PerCP-Cy5.5": {"laser": "Blue (488)", "si_rank": 4}, "PE-Cy7": {"laser": "Blue (488)", "si_rank": 8},
            "7-AAD": {"laser": "Blue (488)", "si_rank": 6},
            "PE-Texas Red": {"laser": "Yellow-Green (561)", "si_rank": 7}, "APC-R700": {"laser": "Yellow-Green (561)", "si_rank": 6},
            "APC": {"laser": "Red (640)", "si_rank": 8}, "Alexa Fluor 700": {"laser": "Red (640)", "si_rank": 6},
            "APC-Cy7": {"laser": "Red (640)", "si_rank": 7}, "Zombie NIR": {"laser": "Red (640)", "si_rank": 7},
            "UV395": {"laser": "UV (355)", "si_rank": 8}, "Pacific Blue": {"laser": "UV (355)", "si_rank": 7},
        }
        INSTRUMENT_SLOTS = {
            "UV (355)": {"capacity": 2, "used": []}, "Violet (405)": {"capacity": 4, "used": []},
            "Blue (488)": {"capacity": 4, "used": []}, "Yellow-Green (561)": {"capacity": 3, "used": []},
            "Red (640)": {"capacity": 3, "used": []},
        }

        # --- 解析表格输入 & 智能识别 ---
        antigen_list = []
        valid_rows = edited_df[edited_df['抗原'].notna() & (edited_df['抗原'] != "")]
        
        # 关键修复：在这里进行智能识别
        for index, row in valid_rows.iterrows():
            antigen = row['抗原']
            strength = row['强度']
            # 如果强度是默认的"中等"，则尝试自动识别
            if strength == "中等 (Medium)":
                strength = auto_detect_strength(antigen)
            antigen_list.append((antigen, strength))
            
        if not antigen_list:
            st.warning("请在表格中输入至少一个抗原！")
        else:
            # --- 运行核心逻辑 ---
            result, status = run_allocation_logic(selected_live_dead, antigen_list, FLUOROPHORE_DB, INSTRUMENT_SLOTS)

            # --- 展示结果 ---
            if status == "成功":
                st.success("配色方案生成成功！")
                result_data = []
                for ag, dye in result.items():
                    laser = FLUOROPHORE_DB.get(dye, {}).get("laser", "N/A")
                    result_data.append({"抗原": ag, "推荐染料": dye, "激光器": laser})
                
                st.dataframe(pd.DataFrame(result_data), use_container_width=True)
            else:
                st.error(status)
