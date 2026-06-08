import pandas as pd
from pathlib import Path


def load_data(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"The file '{file_path}' does not exist."
        )

    df = pd.read_csv(file_path)
    return df


def show_dataset_info(df):
    info = "\n=========== Dataset Information ===========\n"

    info += f"Number of rows: {df.shape[0]}\n"
    info += f"Number of columns: {df.shape[1]}\n\n"

    info += "Column names:\n"
    for col in df.columns:
        info += f"  - {col}\n"

    info += "\nData types:\n"
    for col in df.columns:
        info += f"  - {col}: {df[col].dtype}\n"

    return info
