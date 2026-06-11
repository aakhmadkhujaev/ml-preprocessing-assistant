import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
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

def one_hot_encode(df):
    encoded_df = df.copy()

    categorical_columns = encoded_df.select_dtypes(
        exclude="number"
    ).columns

    encoded_df = pd.get_dummies(
        encoded_df,
        columns=categorical_columns,
        drop_first=True
    )

    return encoded_df

def label_encode(df):
    encoded_df = df.copy()

    categorical_columns = encoded_df.select_dtypes(
        exclude="number"
    ).columns

    for col in categorical_columns:
        encoder = LabelEncoder()
        encoded_df[col] = encoder.fit_transform(
            encoded_df[col]
        )

    return encoded_df

def encode_dataset(df, method):

    if method == "onehot":
        return one_hot_encode(df)

    elif method == "label":
        return label_encode(df)

    elif method == "skip":
        return df.copy()

    else:
        raise ValueError("Invalid encoding method.")