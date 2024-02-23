import pandas as pd
import os


def load_csv(path: str) -> pd.DataFrame:
    """Loads a csv file into a pandas DataFrame."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    assert path.endswith(".csv"), f"File is not a csv: {path}"
    return pd.read_csv(path, header=0)
