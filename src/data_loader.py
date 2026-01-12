import pandas as pd
import os

DATA_PATH = os.path.join("data", "sample_ashrae.csv")

def load_raw_data():
    return pd.read_csv(DATA_PATH)
