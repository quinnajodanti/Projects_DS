# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:52:44 2021

@author: Hp
"""
import numpy as np
import pickle
import streamlit as st
#from fastapi import FastAPI
#import joblib,os

#app = FastAPI()

#pkl
#phish_model = open('phishing.pkl','rb')
#phish_model_ls = joblib.load(phish_model)
#loading the model

loaded_model = pickle.load(open('D:/Downloads/Phishing Site URLs Prediction/phishing.pkl','rb'))
# ML Aspect
#@app.get('/predict/{feature}')
def predict(features):
	X_predict = []
	X_predict.append(str(features))
	y_Predict = loaded_model.predict(X_predict)
	if y_Predict == 'bad':
		result = "This is a Phishing Site"
	else:
		result = "This is not a Phishing Site"

	return (features, result)


def main():
    #giving title
    st.title('Phising Site Predicting App')
    #getting input from user
    url = st.text_input('Website url')
    
    predicted =''
    #creating button for prediction
    if st.button('Predict Website Result'):
        predicted = predict(url)
        
    st.success(predicted)
    
    
if __name__ == '__main__':
	main()
    
#uvicorn prediction_app:app --reload
    
    