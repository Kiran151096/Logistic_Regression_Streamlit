# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 19:49:47 2025

@author: kiran
"""
import streamlit as st
import math
import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.header("🚢 Titanic Survival Prediction")

col1, col2, col3 = st.columns(3)
with col1:
    Pclass = st.selectbox("Class of Passenger", ("Premiere", "Executive", "Economy"))
with col2:
    Sex = st.selectbox("Gender", ("Male", "Female"))
with col3:
    Age = st.number_input("Age of Passenger", min_value=0)

col4, col5 = st.columns(2)
with col4:
    Sibsp = st.number_input("Siblings/Spouses", min_value=0)
with col5:
    Parch = st.number_input("Parents/Children", min_value=0)

col7, col8 = st.columns(2)
with col7:
    Fare = st.number_input("Fare of Journey", min_value=0.0)
with col8:
    Embarked = st.selectbox("Picking Point", ("Cherbourg", "Queenstown", "Southampton"))

if st.button("Predict"):

    # Convert categorical values
    Pclass = 1 if Pclass == "Premiere" else (2 if Pclass == "Executive" else 3)
    Gender = 1 if Sex == "Male" else 0

    # Convert Embarked to One-Hot Encoding
    Embarked_C = 1 if Embarked == "Cherbourg" else 0
    Embarked_Q = 1 if Embarked == "Queenstown" else 0
    

    # Round values
    Age = math.ceil(Age)
    Sibsp = math.ceil(Sibsp)
    Parch = math.ceil(Parch)
    Fare = math.ceil(Fare)

    # Make Prediction
    result = model.predict([[Pclass, Gender, Age, Sibsp, Parch, Fare, Embarked_C, Embarked_Q]])

    output_labels = {
        1: "✅ The passenger will Survive",
        0: "❌ The passenger will not Survive"
    }

    st.markdown(f"## {output_labels[result[0]]}")
