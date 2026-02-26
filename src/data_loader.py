# import pandas as pd
# import os

import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "sample_ashrae.csv")

def load_raw_data():
    return pd.read_csv(DATA_PATH)

