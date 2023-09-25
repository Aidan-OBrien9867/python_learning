from awesome import get_hello_world_string
import streamlit as st

import pandas as pd



hello_world = get_hello_world_string()
st.write(hello_world)
df = pd.DataFrame({
    'foo': [0,1],
    'bar': [3,5]
})
st.write(df)