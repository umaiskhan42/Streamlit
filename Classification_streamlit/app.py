import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris=load_iris()
    df=pd.DataFrame(iris.data,columns=iris.feature_names)
    df['species']=iris.target
    return df, iris.target_names 

df,target_names=load_data()

model=RandomForestClassifier()
model.fit(df.iloc[::-1],df['species'])

st.sidebar.title("Input Features")

sepal_l=st.sidebar.slider("Sepal Length",float(df['sepal length (cm)'].min(),float(df['sepal length (cm)'].max())))
sepal_w=st.sidebar.slider("Sepal Width",float(df['sepal width (cm)'].min(),float(df['sepal width (cm)'].max())))

petal_l=st.sidebar.slider("Petal Length",float(df['petal length (cm)'].min(),float(df['petal length (cm)'].max())))

petal_w=st.sidebar.slider("Sepal Width",float(df['petal width (cm)'].min(),float(df['petal width (cm)'].max())))

input_data=[[sepal_l,sepal_w,petal_l,petal_w]]               

#prediction

prediction=model.predict(input_data)
pred=target_names(prediction[0])

st.write("The predicted species is {pred}")