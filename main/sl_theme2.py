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
    st.html(
        """
        <style>
        body {
            background-color: #FFFFFF;
            color: #000000;
        }
        </style>
        """
    )
else:
    st.html(
        """
        <style>
        body {
            background-color: #000000;
            color: #FFFFFF;
        }
        </style>
        """
    )

# コンテンツ
st.title("テーマ切り替えのサンプル")
st.html("このサンプルでは、ライトモードとダークモードを切り替えることができます。")
# st.html('<div class="custom-body">このサンプルでは、ライトモードとダークモードを切り替えることができます。</div>')