import streamlit as st

# ページの基本設定
st.set_page_config(
    page_title="テーマ切り替えサンプル",
    layout="centered",
)

# テーマ選択
theme = st.selectbox("テーマを選択してください", ["ライトモード", "ダークモード"])

# CSSでライトモードとダークモードの切り替え
if theme == "ライトモード":
    custom_css = """
    <style>
    body {
        background-color: #FFFFFF;
        color: #000000;
    }
    .custom-body {
        background-color: #FFFFFF;
        color: #000000;
    }
    </style>
    """
else:
    custom_css = """
    <style>
    body {
        background-color: #000000;
        color: #FFFFFF;
    }
    .custom-body {
        background-color: #000000;
        color: #FFFFFF;
    }
    </style>
    """

# Inject CSS into the app
st.markdown(custom_css, unsafe_allow_html=True)

# コンテンツ
st.title("テーマ切り替えのサンプル")
st.markdown('<div class="custom-body">このサンプルでは、ライトモードとダークモードを切り替えることができます。</div>', unsafe_allow_html=True)
