import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "thermal_comfort_model.pkl")

FEATURE_COLUMNS = [
    "Air temperature (C)",
    "Relative humidity (%)",
    "Air velocity (m/s)",
    "Radiant temperature (C)",
    "Clo",
    "Met"
]

class ThermalComfortDigitalTwin:
    def __init__(self):
        self.model = None

    def load_model(self):
        if self.model is None:
            self.model = joblib.load(MODEL_PATH)

    def predict(self, inputs: dict):
        self.load_model()
        df = pd.DataFrame([inputs], columns=FEATURE_COLUMNS)
        return self.model.predict(df)[0]
