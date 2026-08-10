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
    with open(PASSWORD_FILE, "r") as f:
        saved_password = json.load(f).get("password")

# 3. 检查是否已登录
if not st.session_state.is_logged_in:
    st.set_page_config(page_title="My Bio-Tools", page_icon="🔬")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # 场景 A：需要修改密码
        if st.session_state.needs_password_change:
            st.title("🔑 首次登录安全设置")
            st.warning("检测到您正在使用初始密码，为了安全起见，请设置一个复杂的新密码。")
            
            new_pwd = st.text_input("新密码", type="password", key="new_pwd")
            confirm_pwd = st.text_input("确认新密码", type="password", key="confirm_pwd")
            
            if st.button("确认修改", type="primary"):
                # 校验密码复杂度：大于8位，且包含字母和数字
                has_alpha = any(c.isalpha() for c in new_pwd)
                has_digit = any(c.isdigit() for c in new_pwd)
                is_long_enough = len(new_pwd) >= 8
                
                if not (has_alpha and has_digit and is_long_enough):
                    st.error("❌ 密码太简单！要求：至少8位，且必须同时包含字母和数字。")
                elif new_pwd != confirm_pwd:
                    st.error("❌ 两次输入的密码不一致，请重试。")
                else:
                    # 保存新密码
                    with open(PASSWORD_FILE, "w") as f:
                        json.dump({"password": new_pwd}, f)
                    st.session_state.needs_password_change = False
                    st.session_state.is_logged_in = True
                    st.success("密码设置成功！正在进入系统...")
                    st.rerun()

        # 场景 B：正常的登录界面
        else:
            st.title("🔒 私人生物工具箱")
            st.caption("请输入访问密码以继续")
            
            password = st.text_input("访问密码", type="password", key="pwd_input")
            
            if st.button("🔓 解锁进入", type="primary"):
                # 判断密码是否匹配（优先匹配修改后的密码，其次匹配初始密码）
                if password == saved_password or password == INITIAL_PASSWORD:
                    st.session_state.is_logged_in = True
                    # 如果用的是初始密码，强制要求改密
                    if password == INITIAL_PASSWORD:
                        st.session_state.needs_password_change = True
                    st.rerun()
                else:
                    st.error("❌ 密码错误，请重试。")
    
    st.stop()  # 未登录状态下，阻止后续代码运行

# ================= 下面是你原来的主页代码 =================
st.set_page_config(page_title="My Bio-Tools", page_icon="🧬", layout="wide")
st.title("🧬 My Bio-Tools 主页")
st.markdown("欢迎回来！请选择你需要使用的工具：")
st.divider()

# 定义工具列表数据
tools_data = [
    {"title": "IC50 剂量反应曲线分析", "desc": "Page 1 - 工具一", "icon": "📊", "page": "pages/page1.py"},
    {"title": "流式配色智能小助手", "desc": "Page 2 - 工具二", "icon": "🎨", "page": "pages/page2.py"},
    {"title": "EC50 剂量反应曲线分析", "desc": "Page 3 - 工具三", "icon": "📈", "page": "pages/page3.py"},
    {"title": "生物科研全能工具箱", "desc": "Page 4 - 工具四", "icon": "🧬", "page": "pages/page4.py"},
    {"title": "荧光基团光谱查询工具", "desc": "Page 5 - 工具五", "icon": "💡", "page": "pages/page5.py"},
]

# 第一排：3个工具
cols_row1 = st.columns(3)
for i in range(3):
    with cols_row1[i]:
        tool = tools_data[i]
        st.metric(label=tool["icon"], value=tool["title"])
        st.caption(tool["desc"])
        if st.button(f"打开 {tool['title']}", key=f"btn_{i}"):
            st.switch_page(tool["page"])

st.divider()

# 第二排：2个工具 (居中)
cols_row2 = st.columns([1, 1, 1])
with cols_row2[0]:
    tool = tools_data[3]
    st.metric(label=tool["icon"], value=tool["title"])
    st.caption(tool["desc"])
    if st.button(f"打开 {tool['title']}", key=f"btn_{3}"):
        st.switch_page(tool["page"])

with cols_row2[1]:
    tool = tools_data[4]
    st.metric(label=tool["icon"], value=tool["title"])
    st.caption(tool["desc"])
    if st.button(f"打开 {tool['title']}", key=f"btn_{4}"):
        st.switch_page(tool["page"])

st.markdown("---")
st.caption("© 2024 My Bio-Tools Private Station")
