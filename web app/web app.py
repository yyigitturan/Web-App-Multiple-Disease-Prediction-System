# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:10:46 2023

@author: yigit_5rkz30x
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open("C:/Users/yigit_5rkz30x/ML Project/Multiple Disease Prediction System/saved models/diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(open("C:/Users/yigit_5rkz30x/ML Project/Multiple Disease Prediction System/saved models/heart_disease_model.sav", "rb"))
parkinsons_model = pickle.load(open("C:/Users/yigit_5rkz30x/ML Project/Multiple Disease Prediction System/saved models/parkinsons_model.sav", "rb"))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System Using ML',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        glucose = st.text_input('Glucose level')
    with col3:
        blood_pressure = st.text_input('Blood Pressure value')
    with col1:
        skin_thickness = st.text_input('Skin Thickness value')
    with col2:
        insulin = st.text_input('Insulin level')
    with col3:
        bmi = st.text_input('BMI value')
    with col1:
        diabetes_pedigree_function = st.text_input('Diabetes Pedigree Function value')
    with col2:
        age = st.text_input('Age of the person')

    # Code for prediction
    diab_diagnosis = ''

    # Creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is not Diabetic'
    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.selectbox('Sex', [0, 1])

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        age = int(age)
        sex = int(sex)
        cp = int(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = int(fbs)
        restecg = int(restecg)
        thalach = float(thalach)
        exang = int(exang)
        oldpeak = float(oldpeak)
        slope = int(slope)
        ca = int(ca)
        thal = int(thal)

        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


# Parkinson's Prediction Page
if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        rap = st.text_input('MDVP:RAP')

    with col2:
        ppq = st.text_input('MDVP:PPQ')

    with col3:
        ddp = st.text_input('Jitter:DDP')

    with col4:
        shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        apq3 = st.text_input('Shimmer:APQ3')

    with col2:
        apq5 = st.text_input('Shimmer:APQ5')

    with col3:
        apq = st.text_input('MDVP:APQ')

    with col4:
        dda = st.text_input('Shimmer:DDA')

    with col5:
        nhr = st.text_input('NHR')

    with col1:
        hnr = st.text_input('HNR')

    with col2:
        rpde = st.text_input('RPDE')

    with col3:
        dfa = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        d2 = st.text_input('D2')

    with col2:
        ppe = st.text_input('PPE')

    # Code for Prediction
    parkinsons_diagnosis = ''

    # Creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
