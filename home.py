
import streamlit as st

# --- 页面基础配置 ---
st.set_page_config(
    page_title="My Bio-Tools 主页",
    page_icon="🧬",
    layout="wide"
)

# --- 自定义 CSS 样式 (让卡片更好看) ---
st.markdown("""
<style>
    /* 卡片容器样式 */
    .tool-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
        height: 100%;
        transition: transform 0.2s;
    }
    /* 鼠标悬停效果 */
    .tool-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    /* 标题样式 */
    .card-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    /* 描述文字样式 */
    .card-desc {
        color: #666;
        font-size: 1rem;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- 主页头部 ---
st.title("🧬 My Bio-Tools 生物数据分析平台")
st.markdown("欢迎使用！请点击下方卡片进入相应的分析工具。")
st.divider()

# --- 第一排：3列布局 ---
col1, col2, col3 = st.columns(3)

# === 工具 1 (对应 page1.py) ===
with col1:
    st.markdown("""
    <div class="tool-card">
        <div class="card-title">📊 IC50剂量反应曲线分析工具</div>
        <p class="card-desc">单组数据的剂量-反应曲线拟合，快速计算 IC50 值。</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("进入工具 1", key="btn1", use_container_width=True):
        st.switch_page("pages/page1.py")

# === 工具 2 (对应 page2.py) ===
with col2:
    st.markdown("""
    <div class="tool-card">
        <div class="card-title">🎨 流式配色智能小助手</div>
        <p class="card-desc">流式细胞术荧光配色方案推荐与优化，一键生成最佳荧光组合。</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("进入工具 2", key="btn2", use_container_width=True):
        st.switch_page("pages/page2.py")

# === 工具 3 (对应 page3.py) ===
with col3:
    st.markdown("""
    <div class="tool-card">
        <div class="card-title">📈 EC50剂量反应曲线分析工具</div>
        <p class="card-desc">支持多化合物横向排版模板，自动批量计算 EC50 并生成报告。</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("进入工具 3", key="btn3", use_container_width=True):
        st.switch_page("pages/page3.py")

# --- 第二排：2列布局（居中） ---
col4, col5 = st.columns(2)

# === 工具 4 (对应 page4.py) ===
with col4:
    st.markdown("""
    <div class="tool-card">
        <div class="card-title">🔬 生物科研全能工具箱</div>
        <p class="card-desc">汇集多种生物科研常用计算工具，涵盖分子量、浓度稀释、缓冲液配制等。</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("进入工具 4", key="btn4", use_container_width=True):
        st.switch_page("pages/page4.py")

# === 工具 5 (对应 page5.py) ===
with col5:
    st.markdown("""
    <div class="tool-card">
        <div class="card-title">💡 荧光基团光谱查询工具</div>
        <p class="card-desc">查询荧光基团的激发光和发射光波长，支持模糊搜索，快速定位所需荧光染料。</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("进入工具 5", key="btn5", use_container_width=True):
        st.switch_page("pages/page5.py")

# --- 页脚 ---
st.divider()
st.caption("Powered by Streamlit | Developed for Bio-Analysis")
