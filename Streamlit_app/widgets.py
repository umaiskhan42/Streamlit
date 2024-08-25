import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")
name=st.text_input("Enter your name")

age=st.slider("write you age",0,100,5)

st.write(f"Your age is {age}")

options=['male','female']
choice=st.selectbox("choose your gender",options)

st.write(f"Your gender is {choice}")

if name:
    st.write(f"Hello {name}")

uploaded_file=st.file_uploader("Choose a csv file: ",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)