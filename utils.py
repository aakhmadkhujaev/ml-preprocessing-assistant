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

def analyze_missing_values(df):
    missing_info = "\n=========== Missing Values Analysis ===========\n"
    missing_by_column = df.isnull().sum()
    missing_values = missing_by_column[missing_by_column > 0]
    if missing_values.empty:
        missing_info += "No missing values found in the dataset.\n"
    else:
        missing_info += "Missing values by column:\n"
        for col, count in missing_values.items():
            missing_info += f"  - {col}: {count} missing values\n"
    return missing_info

def analyze_duplicates(df):
    duplicate_info = "\n=========== Duplicate Analysis ===========\n"
    duplicate_count = df.duplicated().sum()
    if duplicate_count == 0:
        duplicate_info += "No duplicate rows found in the dataset.\n"
    else:
        duplicate_info += f"Number of duplicate rows: {duplicate_count}\n"
        duplicate_info += "Duplicate rows (first 5):\n"
        duplicate_rows = df[df.duplicated()]
        for index, row in duplicate_rows.head(5).iterrows():
            duplicate_info += f"Row {index}: {row.to_dict()}\n"
    return duplicate_info

def save_dataset(df, output_path):
    output_path = Path(output_path)
    df.to_csv(output_path, index=False)
    print(f"Dataset saved to '{output_path}'")
