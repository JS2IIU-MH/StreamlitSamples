import streamlit as st
import pandas as pd

# ファイルアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

# ファイルがアップロードされた場合
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, index_col=0)
    st.write("アップロードされたデータフレーム:")
    st.write(df)

    # 簡単なデータ処理
    processed_df = df.describe()

    # 処理結果を表示
    st.write("処理されたデータフレーム:")
    st.write(processed_df)

    # 処理結果をCSVとしてダウンロード
    csv = processed_df.to_csv().encode('utf-8')
    st.download_button(
        label="処理結果をダウンロード",
        data=csv,
        file_name='processed_data.csv',
        mime='text/csv',
    )