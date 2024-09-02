import streamlit as st
import pandas as pd

# ファイルアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

# ファイルがアップロードされた場合
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("アップロードされたデータフレーム:")
    st.write(df)