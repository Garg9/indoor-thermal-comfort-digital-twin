import pandas as pd

FEATURE_COLUMNS = [
    "Air temperature (C)",
    "Relative humidity (%)",
    "Air velocity (m/s)",
    "Radiant temperature (C)",
    "Clo",
    "Met"
]

TARGET_COLUMN = "Thermal comfort"

def preprocess_data(df: pd.DataFrame):
    df = df[FEATURE_COLUMNS + [TARGET_COLUMN]].dropna()
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]
    return X, y
