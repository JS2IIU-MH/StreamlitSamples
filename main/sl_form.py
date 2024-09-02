import streamlit as st

# フォームの作成
with st.form("my_form"):
    name = st.text_input("名前を入力してください")
    age = st.number_input("年齢を入力してください", min_value=0, max_value=120)

    # 送信ボタン
    submitted = st.form_submit_button("送信")

# フォームが送信された後の処理
if submitted:
    st.write(f"こんにちは、{name}さん。あなたは{age}歳です。")