import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw/ashrae_db2.01.csv")

def load_raw_data():
    """
    Load the raw ASHRAE thermal comfort dataset.
    """
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            "Dataset not found. Please place ashrae_db.01.csv in data/raw/"
        )
    
    df = pd.read_csv(DATA_PATH)
    return df
