import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# set page configuration
st.set_page_config(page_title="Health Guard",layout = "wide")

# Path of working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading of the saved models
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction',],menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    
    # page title
    st.title('Diabetes Prediction Using ML')

    # getting the input data from the user 
    col1,col2,col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        glucose = st.text_input('Glucose Level')
    with col3:
        bloodpressure =  st.text_input('Blood Pressure Value')    

    with col1:
        skinthickness = st.text_input('Skin Thickness Value')
    with col2:
        insulin = st.text_input('Insulin Level')
    with col3:
        bmi =  st.text_input('BMI Value')

    with col1:
        dpf = st.text_input('Diabetes Pedigree Function')
    with col2:
        age = st.text_input('Age of the Person')

    # backend logic
    diab_diagnosis = ''   # this is empty string for further storing the values

    # creation of a button 
    
    if st.button('Diabetes Test Result'):
        input = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]

        input = [float(x) for x in input]

        diab_prediction = diabetes_model.predict([input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    
    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    
    # page title
    st.title('Heart Disease Prediction Using ML')

    # getting the input data from the user 
    col1,col2,col3 = st.columns(3)

    #row1
    with col1:
        age = st.text_input('Age')
    with col2:
        gender = st.text_input('Gender')
    with col3:
        cp =  st.text_input('Chest Pain Type')  

    #row2  

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dl')
    with col3:
        fbs =  st.text_input('Fasting Blood Sugar')

    #row3

    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
    with col2:
        mhra = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        eia =  st.text_input('Exercise Induced Angina')

    #row4

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of peak exercise ST segement')
    with col3:
        mvcf =  st.text_input('Major vessels colored by flouroscopy')

    #row5

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    # backend logic
    heart_diagnosis = ''   # this is empty string for further storing the values

    # creation of a button 
    
    if st.button('Heart Test Result'):
        input = [age,gender,cp,trestbps,chol,fbs,restecg,mhra,eia,oldpeak,slope,mvcf,thal]

        input = [float(x) for x in input]

        heart_prediction = heart_disease_model.predict([input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having Heart Disease'
        else:
            diab_diagnosis = 'The person is not having Heart Disease'
    
    st.success(heart_diagnosis)

    



    

    

    





