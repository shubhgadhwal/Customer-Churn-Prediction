import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
import pandas as pd
import pickle

model = tf.keras.models.load_model('model.h5')
with open('onehot_encoder_geo.pkl','rb') as file:
    geo_encode = pickle.load(file)
with open('label_encoder_gender.pkl','rb') as file:
    gender_encode = pickle.load(file)
with open('scaler.pkl','rb') as file:
    scale = pickle.load(file)

st.title('Customer Churn Prediction')
geography=st.selectbox('Geography',geo_encode.categories_[0])
gender  = st.selectbox('Gender',gender_encode.classes_)
age=st.slider('Age',18,92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary=st.number_input('Estimated Salary')
tenure = st.slider('Tenure',0,10)
num_of_products = st.slider('Number of Products',1,4)
has_cr_Card = st.selectbox('Has Credit Card',[0,1])
is_active_member = st.selectbox('Is active Member?',[0,1])