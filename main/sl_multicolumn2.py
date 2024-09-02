import streamlit as st

# カスタム幅のカラムを作成
col1, col2, col3 = st.columns([3, 1, 1])

with col1:
    st.header("カラム 1 (幅3)")
    st.write("こちらはカラム1の内容です。")

with col2:
    st.header("カラム 2 (幅1)")
    st.write("こちらはカラム2の内容です。")

with col3:
    st.header("カラム 3 (幅1)")
    st.write("こちらはカラム3の内容です。")