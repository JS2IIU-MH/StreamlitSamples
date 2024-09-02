import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
print(map_data)

# https://www.google.com/maps/@35.2834003,136.8960406,17.08z?authuser=0&entry=ttu
# map_data2 = pd.DataFrame(
#     ([35.2834003], [136.8960406]),
#     columns=['lat', 'lon'])
map_data2 = pd.DataFrame()
map_data2['lat'] = [35.2834003]
map_data2['lon'] = [136.8960406]
print(map_data2)
st.map(map_data2)
