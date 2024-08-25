import streamlit as st
import numpy as np
import pandas as pd

#Title of app
st.title("Streamlit app")

# Display simple text

st.write("This is the text")

# Create a dataframe

df=pd.DataFrame({
    'Column A': [1,2,3,4],
    'Column B': [3,5,7,8]
})

# Display the dataframe
st.write("here is the dataframe")
st.write(df)