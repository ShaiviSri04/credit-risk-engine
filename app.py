from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load everything
model = pickle.load(open("xgb_model.pkl","rb"))
columns = pickle.load(open("columns.pkl","rb"))
education_map = pickle.load(open("education_map.pkl","rb"))
risk_policy = pickle.load(open("risk_policy.pkl","rb"))

def assign_risk(pd):
    if pd < risk_policy["low"]:
        return "Low Risk","Approve"
    elif pd < risk_policy["medium"]:
        return "Medium Risk","Review"
    else:
        return "High Risk","Reject"

@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="POST":
        data = request.form.to_dict()
        df = pd.DataFrame([data])

        # Convert to numeric
        df = df.apply(pd.to_numeric, errors='ignore')

        # EDUCATION mapping
        if 'EDUCATION' in df.columns:
            df['EDUCATION'] = df['EDUCATION'].map(education_map)

        # One-hot encode
        df = pd.get_dummies(df)

        # Align with training columns
        for col in columns:
            if col not in df.columns:
                df[col] = 0

        df = df[columns]

        pd_score = model.predict_proba(df)[0][1]
        band,decision = assign_risk(pd_score)

        return render_template("index.html",
                               pd=round(pd_score,3),
                               band=band,
                               decision=decision)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

