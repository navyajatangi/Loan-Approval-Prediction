import streamlit as st
import pandas as pd
import joblib

# Load files
model = joblib.load("SVC.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.set_page_config(page_title="Loan Approval Prediction")

st.title("🏦 Loan Approval Prediction")

st.write("Enter Applicant Details")

# Inputs

gender = st.selectbox("Gender", ["Male", "Female"])

married = st.selectbox("Married", ["Yes", "No"])

dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])

education = st.selectbox("Education", ["Graduate", "Not Graduate"])

self_emp = st.selectbox("Self Employed", ["Yes", "No"])

app_income = st.number_input("Applicant Income", 0)

co_income = st.number_input("Coapplicant Income", 0)

loan_amount = st.number_input("Loan Amount", 0)

loan_term = st.number_input("Loan Amount Term", 360)

credit_history = st.selectbox("Credit History", [1.0, 0.0])

property_area = st.selectbox("Property Area",
                             ["Urban", "Semiurban", "Rural"])

if st.button("Predict"):

    data = {
        "ApplicantIncome":[app_income],
        "CoapplicantIncome":[co_income],
        "LoanAmount":[loan_amount],
        "Loan_Amount_Term":[loan_term],
        "Credit_History":[credit_history],
        "Gender_Male":[1 if gender=="Male" else 0],
        "Married_Yes":[1 if married=="Yes" else 0],
        "Dependents_1":[1 if dependents=="1" else 0],
        "Dependents_2":[1 if dependents=="2" else 0],
        "Dependents_3+":[1 if dependents=="3+" else 0],
        "Education_Not Graduate":[1 if education=="Not Graduate" else 0],
        "Self_Employed_Yes":[1 if self_emp=="Yes" else 0],
        "Property_Area_Semiurban":[1 if property_area=="Semiurban" else 0],
        "Property_Area_Urban":[1 if property_area=="Urban" else 0],
    }

    input_df = pd.DataFrame(data)

    # Match training columns
    input_df = input_df.reindex(columns=columns, fill_value=0)

    scaled = scaler.transform(input_df)

    prediction = model.predict(scaled)[0]

    if prediction == "Y":
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    