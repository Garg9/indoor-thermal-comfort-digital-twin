from flask import Flask, render_template, request
import pandas as pd

from src.data_loader import load_raw_data
from src.preprocessing import preprocess_data
from src.model_training import train_models

app = Flask(__name__)

# ------------------- Train Model ONCE -------------------
print("Training model...")
df = load_raw_data()
X, y = preprocess_data(df)
model = train_models(X, y)
print("Model trained successfully!")

# ------------------- Routes -------------------

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probabilities = None

    if request.method == "POST":
        ta = float(request.form["ta"])
        rh = float(request.form["rh"])
        v = float(request.form["v"])
        tr = float(request.form["tr"])
        clo = float(request.form["clo"])
        met = float(request.form["met"])

        input_df = pd.DataFrame([{
            "Air temperature (C)": ta,
            "Relative humidity (%)": rh,
            "Air velocity (m/s)": v,
            "Radiant temperature (C)": tr,
            "Clo": clo,
            "Met": met
        }])

        prediction = model.predict(input_df)[0]
        probabilities = model.predict_proba(input_df)[0]

        # ---------------- Digital Twin Rule Override ----------------
        if ta >= 30 and v <= 0.15 and clo >= 0.8:
            prediction = "Warm"
        elif ta <= 18 and v >= 0.25:
            prediction = "Cold"

    return render_template(
        "index.html",
        prediction=prediction,
        probabilities=probabilities
    )

if __name__ == "__main__":
    app.run(debug=True)
