# 🧠 Credit Risk Decision Engine

**End-to-End Machine Learning, Explainability & Fintech Underwriting Platform**

A **production-grade credit risk scoring system** that predicts the **Probability of Default (PD)** for loan applicants using **XGBoost**, validates the model using **industry-standard risk metrics**, explains predictions using **SHAP**, and deploys the model as a **real-time underwriting web application**.

**Live System:**
👉 [https://credit-risk-engine.onrender.com](https://credit-risk-engine.onrender.com)

---

# 📌 Business Objective

Banks and fintech lenders must answer one core question:

> “How likely is this applicant to default on their loan?”

This project builds a **machine-learning driven underwriting engine** that:

* Estimates **Probability of Default (PD)**
* Segments borrowers into **risk bands**
* Generates **automated loan decisions**
* Provides **model explainability (SHAP)** for audit & compliance

This mirrors how modern **banks, NBFCs and fintechs** operate in production.

---

# 🧬 Machine Learning Pipeline

This is not a single notebook — it is a **full ML lifecycle**:

```
Raw Credit Bureau Data
        ↓
Data Audit & Cleaning
        ↓
Feature Engineering & Selection
        ↓
Target (Default) Engineering
        ↓
Train Logistic Regression & XGBoost
        ↓
Evaluate with ROC-AUC, PR-AUC, KS
        ↓
Model Explainability (SHAP)
        ↓
Risk Policy & Banding
        ↓
Flask API
        ↓
Cloud Deployment (Render)
```

---

# 📊 Data & Feature Engineering

### Data Processing

* Missing values handled using:

  * Median (numerical)
  * Mode (categorical)
* Outliers capped using percentile-based clipping
* Categorical variables encoded using:

  * Education mapping
  * One-hot encoding for model compatibility

### Feature Engineering

Engineered financial risk indicators:

* Credit history age
* Recent enquiry intensity
* Delinquency severity
* Income-to-risk relationship
* Behavioural stability signals

Features were selected based on:

* Correlation with default
* Information value
* Model contribution (via SHAP)

---

# 🎯 Target Engineering (Default Flag)

The binary target variable was engineered to represent:

> **1 = Default (Bad Borrower)**
> **0 = Non-Default (Good Borrower)**

This reflects real-world credit bureau definitions used in banking.

---

# 🤖 Model Training

Two models were trained:

| Model               | Purpose                                |
| ------------------- | -------------------------------------- |
| Logistic Regression | Baseline risk score                    |
| XGBoost             | Production-grade non-linear risk model |

XGBoost was chosen because:

* Handles **non-linear interactions**
* Works well on **imbalanced data**
* Industry standard in **credit risk**

---

# 📈 Model Validation (Risk-Industry Metrics)

Models were evaluated using **banking-grade metrics**:

| Metric  | What it Measures                        |
| ------- | --------------------------------------- |
| ROC-AUC | Overall discriminatory power            |
| PR-AUC  | Performance on rare defaulters          |
| KS      | Separation between good & bad borrowers |

### Results

| Model               | ROC-AUC    | PR-AUC     | KS         |
| ------------------- | ---------- | ---------- | ---------- |
| Logistic Regression | 0.9376     | 0.7498     | 0.7300     |
| **XGBoost (Final)** | **0.9376** | **0.8300** | **0.8129** |

Why XGBoost won:

* Higher **PR-AUC** → detects risky borrowers better
* Higher **KS** → stronger segmentation
* Better for real underwriting

---

# 🔍 Model Explainability (SHAP)

SHAP (SHapley Additive exPlanations) was used to:

* Explain **global feature importance**
* Explain **individual loan decisions**
* Validate that model uses **financially sensible drivers**

This is critical for:

* Credit model audits
* Regulatory compliance
* Business trust

Key drivers:

* Delinquency history
* Credit age
* Income
* Enquiry intensity

---

# 🧮 Risk Banding & Business Policy

PD is converted into operational decisions:

| PD     | Risk Band   | Decision      |
| ------ | ----------- | ------------- |
| Low    | Low Risk    | Approve       |
| Medium | Medium Risk | Manual Review |
| High   | High Risk   | Reject        |

These thresholds are stored in `risk_policy.pkl` and applied in production.

---

# 🖥️ Real-Time Credit Scoring App

A full **Flask web application** that:

* Accepts applicant data
* Applies preprocessing
* Runs the XGBoost model
* Returns PD + decision instantly

Tech stack:

* Flask
* XGBoost
* Pandas
* SHAP
* Tailwind CSS
* Gunicorn
* Render

---

# ☁️ Cloud Deployment

The system is deployed on **Render** using:

* GitHub CI/CD
* Gunicorn production server
* Environment-aware Flask app

This is a **live fintech-style risk engine**, not a local demo.

---

# 📁 Project Structure

```
credit-risk-engine/
│
├── data/
│   ├── data_dictionary.xlsx
│   ├── model_ready_sample.csv
│   └── pd_model_sample.csv
│
├── notebooks/
│   ├── 01_data_audit_and_cleaning.ipynb
│   ├── 02_feature_engineering_and_selection.ipynb
│   ├── 03_target_engineering.ipynb
│   └── 04_pd_modelling_and_evaluation.ipynb
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── xgb_model.pkl
├── columns.pkl
├── education_map.pkl
├── risk_policy.pkl
└── README.md
```

---

# 🚀 How to Run Locally

```bash
git clone https://github.com/ShaiviSri04/credit-risk-engine.git
cd credit-risk-engine
pip install -r requirements.txt
python app.py
```

Open:
`http://127.0.0.1:5000`

---


