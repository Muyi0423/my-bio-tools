import streamlit as st

# --- 1. 页面基础设置 ---
st.set_page_config(page_title="我的生物信息工具箱", layout="wide", page_icon="🧬")

# --- 2. 核心路由逻辑 (这是最关键的部分) ---
# 检查有没有人按下了按钮
if "page" not in st.session_state:
    st.session_state.page = "home" # 默认显示主页

# 如果 session 里记录了要去 page1，就执行 page1 的代码
if st.session_state.page == "page1":
    # 注意：这里用 exec 运行是为了兼容老版本，如果报错请告诉我
    try:
        exec(open("pages/page1.py", encoding="utf-8").read())
    except Exception as e:
        st.error(f"加载工具失败: {e}")
        if st.button("🏠 返回主页"):
            st.session_state.page = "home"
            st.rerun()
    st.stop() # 执行完 page1 就停止，不要往下跑了

# 如果 session 里记录了要去 page2，就执行 page2 的代码
elif st.session_state.page == "page2":
    try:
        exec(open("pages/page2.py", encoding="utf-8").read())
    except Exception as e:
        st.error(f"加载工具失败: {e}")
        if st.button("🏠 返回主页"):
            st.session_state.page = "home"
            st.rerun()
    st.stop()

# --- 3. 下面是原本的主页界面代码 ---

# 标题部分
st.title("🧬 我的生物信息工具箱")
st.markdown("欢迎使用！请点击下方卡片进入对应工具。")
st.divider()

# 布局：两个并排的列
col1, col2 = st.columns(2)

# === 左边卡片：IC50 高级分析工具 ===
with col1:
    with st.container(border=True):
        st.markdown("### 🧪 IC50 高级分析工具")
        st.caption("用于计算药物的半抑制浓度，支持单组/批量分析及Excel报告导出。")
        
        # 按钮点击后，修改状态为 page1，然后刷新页面
        if st.button("👉 点击进入 IC50 工具", use_container_width=True, type="primary"):
            st.session_state.page = "page1"
            st.rerun()

# === 右边卡片：流式配色智能助手 ===
with col2:
    with st.container(border=True):
        st.markdown("### 🎨 流式配色智能助手")
        st.caption("辅助设计流式细胞术荧光配色方案，告别手动查表。")
        
        # 按钮点击后，修改状态为 page2，然后刷新页面
        if st.button("👉 点击进入流式助手", use_container_width=True, type="primary"):
            st.session_state.page = "page2"
            st.rerun()
