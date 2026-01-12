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
    """
    Clean and prepare data for ML model training.
    """

    # Select required columns
    df = df[FEATURE_COLUMNS + [TARGET_COLUMN]].copy()

    # Remove missing values
    df.dropna(inplace=True)

    # Ensure target is numeric
    # df[TARGET_COLUMN] = pd.to_numeric(df[TARGET_COLUMN], errors="coerce")
    # df.dropna(inplace=True)

    # Convert to comfort classes
    # df["comfort_class"] = df[TARGET_COLUMN].apply(map_comfort_class)

    X = df[FEATURE_COLUMNS]
    y = df["comfort_class"]

    return X, y


def map_comfort_class(value):
    if value <= -1:
        return "Cold"
    elif value >= 1:
        return "Warm"
    else:
        return "Neutral"


