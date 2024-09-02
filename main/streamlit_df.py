import pandas as pd
import streamlit as st

# ダミーデータの作成
df = pd.DataFrame({
    '列A': [1, 2, 3],
    '列B': [4, 5, 6]
})

# データフレームの表示
st.dataframe(df)