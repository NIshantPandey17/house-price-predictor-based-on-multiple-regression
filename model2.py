import pickle
import streamlit as st

model1=pickle.load(open("houseprice.pkl","rb"))

def mydeploy():
    st.title("Area Price Prediction")
    area= st.number_input("Enter your area :")
    bedroom= st.number_input("Enter number of bedrooms :")
    age= st.number_input("Enter age of house :")
    pred=st.button("Predict")

    if pred:
        x=model1.predict([[area,bedroom,age]])
        st.write( "Price of area is :",x[0])


 
mydeploy()  