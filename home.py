import streamlit as st
import json
import os

# ================= 🔒 安全配置区域 =================
# 这是出厂初始密码，仅供第一次登录使用
INITIAL_PASSWORD = "123456" 
# 用于保存你修改后的复杂密码的文件
PASSWORD_FILE = "user_password.json"
# ==================================================

# 1. 初始化 Session State
if 'is_logged_in' not in st.session_state:
    st.session_state.is_logged_in = False
if 'needs_password_change' not in st.session_state:
    st.session_state.needs_password_change = False

# 2. 读取已保存的密码（如果存在的话）
saved_password = None
if os.path.exists(PASSWORD_FILE):
    try:
        with open(PASSWORD_FILE, "r") as f:
            saved_password = json.load(f).get("password")
    except Exception:
        saved_password = None

# 确定当前有效的验证密码
current_valid_password = saved_password if saved_password else INITIAL_PASSWORD

# ================= 🛑 拦截逻辑开始 =================

# 情况A：还没登录 -> 显示登录框
if not st.session_state.is_logged_in:
    st.set_page_config(page_title="My Bio-Tools 登录", page_icon="🔒")
    
    # 居中显示登录框
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("🔒 私人生物工具箱")
        st.caption("请输入访问密码")
        
        password_input = st.text_input("密码", type="password", label_visibility="collapsed")
        
        if st.button("进入系统", type="primary", use_container_width=True):
            if password_input == current_valid_password:
                st.session_state.is_logged_in = True
                # 如果是初始密码，标记为需要修改
                if password_input == INITIAL_PASSWORD and not saved_password:
                    st.session_state.needs_password_change = True
                st.rerun()
            else:
                st.error("密码错误，请重试！")
    
    st.stop() # 【关键】没登录时，在这里停止运行，不显示下面的内容

# 情况B：已登录，但需要改密码 -> 显示改密框
if st.session_state.needs_password_change:
    st.set_page_config(page_title="修改密码", page_icon="🔑")
    st.title("🔑 首次登录，请修改密码")
    st.warning("为了安全，请将初始密码修改为复杂密码（至少8位，包含字母和数字）。")
    
    new_pwd = st.text_input("新密码", type="password")
    confirm_pwd = st.text_input("确认新密码", type="password")
    
    if st.button("确认修改", type="primary"):
        if len(new_pwd) < 8:
            st.error("密码长度不能少于8位！")
        elif new_pwd != confirm_pwd:
            st.error("两次输入的密码不一致！")
        elif not any(c.isdigit() for c in new_pwd) or not any(c.isalpha() for c in new_pwd):
            st.error("密码必须同时包含字母和数字！")
        else:
            # 保存新密码到文件
            with open(PASSWORD_FILE, "w") as f:
                json.dump({"password": new_pwd}, f)
            st.success("密码修改成功！正在进入系统...")
            st.session_state.needs_password_change = False
            st.balloons()
            st.sleep(1)
            st.rerun()
    
    st.stop() # 【关键】改密时，也不显示下面的内容

# ================= ✅ 登录成功且无需改密 -> 显示主页 =================

st.set_page_config(page_title="My Bio-Tools", page_icon="🧬", layout="wide")

# 这里放你原来的主页代码（工具卡片布局）
st.title("🧬 My Bio-Tools 生物数据分析平台")
st.markdown("欢迎使用！请点击下方卡片进入相应的分析工具。")
st.divider()

# --- 你的工具布局代码开始 ---
# (这里保留你截图里显示的漂亮布局)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="border:1px solid #e0e0e0; padding:20px; border-radius:10px; height:200px;">
        <h3>📊 IC50剂量反应曲线分析工具</h3>
        <p>单组数据的剂量-反应曲线拟合，快速计算IC50值。</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("进入工具 1", key="b1"):
        st.switch_page("pages/page1.py") # 假设你的工具在 pages 文件夹

with col2:
    st.markdown("""
    <div style="border:1px solid #e0e0e0; padding:20px; border-radius:10px; height:200px;">
        <h3>🎨 流式配色智能小助手</h3>
        <p>流式细胞术荧光配色方案推荐与优化，一键生成最佳荧光组合。</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("进入工具 2", key="b2"):
        st.switch_page("pages/page2.py")

with col3:
    st.markdown("""
    <div style="border:1px solid #e0e0e0; padding:20px; border-radius:10px; height:200px;">
        <h3>📈 EC50剂量反应曲线分析工具</h3>
        <p>支持多化合物横向排版模板，自动批量计算EC50并生成报告。</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("进入工具 3", key="b3"):
        st.switch_page("pages/page3.py")

col4, col5 = st.columns(2)
with col4:
    st.markdown("""
    <div style="border:1px solid #e0e0e0; padding:20px; border-radius:10px; height:200px;">
        <h3>🔬 生物科研全能工具箱</h3>
        <p>汇集多种生物科研常用计算工具，涵盖分子量、浓度稀释、缓冲液配制等。</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("进入工具 4", key="b4"):
        st.switch_page("pages/page4.py")

with col5:
    st.markdown("""
    <div style="border:1px solid #e0e0e0; padding:20px; border-radius:10px; height:200px;">
        <h3>💡 荧光基团光谱查询工具</h3>
        <p>查询荧光基团的激发光和发射光波长，支持模糊搜索，快速定位所需荧光染料。</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("进入工具 5", key="b5"):
        st.switch_page("pages/page5.py")
