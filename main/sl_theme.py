import streamlit as st

# サイドバーにテーマの選択オプションを追加
theme = st.sidebar.radio(
    "テーマを選択してください",
    options=["ライトモード", "ダークモード"]
)

# 選択されたテーマに基づいてスタイルを適用
if theme == "ライトモード":
    st.markdown(
        """
        <style>
        body {
            background-color: #FFFFFF;
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        body {
            background-color: #2c3e50;
            color: #ecf0f1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )