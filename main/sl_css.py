import streamlit as st

# カスタムCSSの適用
st.markdown(
    """
    <style>
    .custom-header {
        font-size: 24px;
        color: #4CAF50;
        text-align: center;
    }
    .custom-container {
        background-color: #f9f9f9;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# カスタムスタイルを適用したヘッダー
st.markdown('<div class="custom-header">カスタムヘッダー</div>', unsafe_allow_html=True)

# カスタムスタイルを適用したコンテナ
with st.container():
    st.markdown('<div class="custom-container">カスタムコンテナ内のコンテンツです。</div>', unsafe_allow_html=True)
    