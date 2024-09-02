import matplotlib.pyplot as plt
import numpy as np

import streamlit as st

# ダミーデータの作成
x = np.linspace(0, 10, 100)
y = np.sin(x)

# グラフの作成
fig, ax = plt.subplots()
ax.plot(x, y)

# Streamlitでグラフを表示
st.write('## Streamlitでグラフを表示')
st.pyplot(fig)