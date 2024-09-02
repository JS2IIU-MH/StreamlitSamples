import streamlit as st
import time

@st.cache_data
def cached_function():
    time.sleep(2)  # シミュレーションとして2秒の遅延
    return "結果"

def non_cached_function():
    time.sleep(2)
    return "結果"

start_time = time.time()
st.write(cached_function())
st.write(f"キャッシュ使用時の処理時間: {time.time() - start_time:.2f}秒")

start_time = time.time()
st.write(non_cached_function())
st.write(f"キャッシュ不使用時の処理時間: {time.time() - start_time:.2f}秒")