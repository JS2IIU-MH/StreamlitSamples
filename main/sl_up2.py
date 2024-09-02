import streamlit as st
import pandas as pd

# 複数ファイルのアップロード
uploaded_files = st.file_uploader("複数のCSVファイルをアップロードしてください", type="csv", accept_multiple_files=True)

# 各ファイルを処理
if uploaded_files:
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        st.write(f"アップロードされたファイル: {uploaded_file.name}")
        st.write(df)