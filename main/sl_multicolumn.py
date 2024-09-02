import streamlit as st

# 2つのカラムを作成
col1, col2 = st.columns(2)

with col1:
    st.header("カラム 1")
    st.write("こちらはカラム1の内容です。")

with col2:
    st.header("カラム 2")
    st.write("こちらはカラム2の内容です。")