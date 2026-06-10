import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
def clean_dataset(df):
    cleaned_df = df.copy()
    cleaned_df = cleaned_df.drop_duplicates()

    numeric_columns = cleaned_df.select_dtypes(include="number").columns
    categorical_columns = cleaned_df.select_dtypes(exclude="number").columns

    for col in numeric_columns:
       median_value = cleaned_df[col].median()
       cleaned_df[col] = cleaned_df[col].fillna(median_value)

    for col in categorical_columns:
       mode_value = cleaned_df[col].mode()[0]
       cleaned_df[col] = cleaned_df[col].fillna(mode_value)

    return cleaned_df

def scale_dataset(df, method):
    scaled_df = df.copy()

    numeric_columns = scaled_df.select_dtypes(
        include="number"
    ).columns

    if method == "standard":
        scaler = StandardScaler()

    elif method == "minmax":
        scaler = MinMaxScaler()

    elif method == "skip":
        return scaled_df

    else:
        raise ValueError(
            "Invalid scaling method."
        )

    scaled_df[numeric_columns] = scaler.fit_transform(
        scaled_df[numeric_columns]
    )

    return scaled_df