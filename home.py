import streamlit as st

# --- 1. 页面设置 ---
st.set_page_config(page_title="我的生物信息工具箱", layout="wide", page_icon="🧰")

# --- 2. 标题 ---
st.title("🧰 我的生物信息工具箱")
st.markdown("欢迎使用！请点击下方卡片进入对应工具。")
st.divider()

# --- 3. 布局：两个并排的列 ---
col1, col2 = st.columns(2)

# === 左边卡片：IC50 (对应 page1) ===
with col1:
    with st.container(border=True):
        st.markdown("### 🧪 IC50 高级分析工具")
        st.caption("用于计算药物的半抑制浓度，支持单组/批量分析及Excel报告导出。")
        
        # 【核心修改】直接使用 streamlit 的页面跳转功能
        # 告诉它：我要去 pages 文件夹下的 page1.py
        # 不需要 os.path，不需要 glob，直接指名道姓！
        if st.button("👉 点击进入 IC50 工具", use_container_width=True, type="primary"):
            st.switch_page("page1.py")

# === 右边卡片：流式配色 (对应 page2) ===
with col2:
    with st.container(border=True):
        st.markdown("### 🎨 流式配色智能助手")
        st.caption("辅助设计流式细胞术荧光配色方案，告别手动查表。")
        
        # 【核心修改】直接指向 page2.py
        if st.button("👉 点击进入流式助手", use_container_width=True, type="primary"):
            st.switch_page("page2.py")
