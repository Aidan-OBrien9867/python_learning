from awesome import get_codeistrash_string
import streamlit as st

import pandas as pd



codeistrash = get_codeistrash_string()
st.write(codeistrash)
df = pd.DataFrame({
    'foo': [0,1],
    'bar': [3,5]
})
st.write(df)