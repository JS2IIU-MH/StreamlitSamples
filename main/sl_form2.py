import streamlit as st

# 複数セクションを持つフォーム
with st.form("detailed_form"):
    # 基本情報セクション
    st.header("基本情報")
    name = st.text_input("名前を入力してください")
    age = st.number_input("年齢を入力してください", min_value=0, max_value=120)

    # 連絡先情報セクション
    st.header("連絡先情報")
    email = st.text_input("メールアドレスを入力してください")
    phone = st.text_input("電話番号を入力してください")

    # 送信ボタン
    submitted = st.form_submit_button("送信")

if submitted:
    st.write(f"こんにちは、{name}さん。あなたは{age}歳です。")
    st.write(f"連絡先情報: {email}, {phone}")