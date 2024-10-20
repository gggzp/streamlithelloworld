import streamlit as st
from wechatpy.oauth import WeChatOAuth
from wechatpy.exceptions import WeChatOAuthException

# 从 Streamlit secrets 中获取配置
APPID = st.secrets["APPID"]
SECRET  = st.secrets["SECRET "]
REDIRECT_URI  = st.secrets["REDIRECT_URI"]
SCOPES = st.secrets["SCOPES"]

# 初始化企业微信OAuth对象
oauth = WeChatOAuth(APPID, SECRET, REDIRECT_URI, SCOPES)



st.title("Hello World")


# 检查是否有code参数
if 'code' in st.experimental_get_query_params():
    code = st.experimental_get_query_params()['code'][0]
    try:
        # 使用code换取access_token
        oauth.fetch_access_token(code)
        # 这里可以获取用户信息，根据需要处理
        user_info = oauth.get_user_info()
        st.write(f"Welcome, {user_info['name']}!")
    except WeChatOAuthException as e:
        st.write(f"An error occurred: {e}")

    # 原始的Streamlit内容
    st.write("This is a simple Streamlit app")
    st.write("Here is a button:")
    if st.button("Click me"):
        st.write("You clicked the button!")
else:
    # 重定向到企业微信认证页面
    auth_url = oauth.authorize_url
    st.write(f"Please authenticate with WeChat Work: [Authenticate]({auth_url})")
