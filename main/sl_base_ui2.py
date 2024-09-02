import streamlit as st

# 年齢の入力
age = st.number_input("年齢を入力してください", min_value=0, max_value=120)

# 条件に応じた動的UI
if age >= 18:
    st.write("あなたは成人です。")
    st.text_input("運転免許証の番号を入力してください")
else:
    st.write("未成年のため、追加情報は必要ありません。")