# 🏦 Loan Approval Prediction

A Machine Learning web application built with **Streamlit** that predicts whether a loan application will be **Approved** or **Rejected** based on applicant details.

---

## 📌 Project Overview

This project uses a trained **Support Vector Classifier (SVC)** model to predict loan approval status. Users enter applicant information through a simple Streamlit interface, and the application returns the prediction instantly.

The project demonstrates:
- Data preprocessing
- Feature engineering
- Feature scaling
- Machine Learning model deployment
- Interactive web application using Streamlit

---

## 🚀 Features

- User-friendly web interface
- Real-time loan approval prediction
- Automatic feature preprocessing
- Uses trained Machine Learning model
- Fast and lightweight deployment

---

## 📂 Project Structure

```
Loan-Approval-Prediction/
│
├── app.py                         # Streamlit application
├── SVC.pkl                        # Trained Support Vector Classifier model
├── scaler.pkl                     # StandardScaler object
├── columns.pkl                    # Training feature columns
├── Loan approval prediction.pkl   # Project notebook/model file
├── requirements.txt               # Required Python libraries
└── README.md                      # Project documentation
```

---

## 📊 Input Features

The application takes the following applicant details:

- Gender
- Married Status
- Dependents
- Education
- Self Employed
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

---

## ⚙️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## 🧠 Machine Learning Model

**Algorithm Used:**
- Support Vector Classifier (SVC)

### Preprocessing Steps

- Missing value handling
- One-Hot Encoding
- Feature Scaling using StandardScaler
- Feature alignment with training columns

---

## ▶️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Loan-Approval-Prediction.git

cd Loan-Approval-Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📷 Application Workflow

```
User Input
      │
      ▼
Feature Encoding
      │
      ▼
Feature Scaling
      │
      ▼
SVC Model Prediction
      │
      ▼
Loan Approved / Loan Rejected
```

---

## 📌 Prediction Output

The application predicts:

- ✅ Loan Approved
- ❌ Loan Rejected

---

## 📈 Future Improvements

- Add probability score
- Deploy on Streamlit Cloud
- Improve UI design
- Support multiple ML models
- Model performance comparison
- Add visual analytics dashboard

---

## 👩‍💻 Author

**Navya**

Machine Learning Enthusiast

---

## 📄 License

This project is developed for educational and learning purposes.
