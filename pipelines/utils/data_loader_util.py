import pandas as pd
from pathlib import Path
import os
BASE_PATH = Path(__file__).resolve().parent.parent.parent  # go 3 levels up to repo root


def load_data(filename: str) -> pd.DataFrame | None:
    try:
        if not isinstance(filename, str):
            raise TypeError("Filename must be a string.")
        file_path = Path(__file__).resolve().parents[2] / "data" / filename  # repo root + data
        if not file_path.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")
        if not file_path.suffix.lower() == ".csv":
            raise ValueError("Only .csv files are allowed.")
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None