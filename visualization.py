import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import seaborn as sns

def plot_missing_values(df):
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    
    if missing_values.empty:
        print("No missing values found.")
        return
    
    plt.figure(figsize=(10, 6))
    missing_values.plot(kind='bar')
    plt.title('Missing Values in Each Column')
    plt.xlabel('Columns')
    plt.ylabel('Number of Missing Values')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plots_folder = Path("output/plots")
    plots_folder.mkdir(parents=True, exist_ok=True)
    plt.savefig(plots_folder / "missing_values.png")
    plt.close()
    print("Plot saved to output/plots/missing_values.png")

def plot_histogram(df, column):

    if column not in df.columns:
        print("Column does not exist.")
        return

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    if column not in numeric_columns:
        print("Histogram only works for numeric columns.")
        return

    plt.figure(figsize=(10, 6))

    df[column].hist()

    plt.title(f"{column} Distribution")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.tight_layout()

    plots_folder = Path("output/plots")
    plots_folder.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        plots_folder / f"{column}_histogram.png"
    )

    plt.close()

def plot_correlation_heatmap(df):

    numeric_df = df.select_dtypes(
    include="number"
    )
    correlation_matrix = numeric_df.corr()

    if numeric_df.empty:
        print(
            "No numeric columns available for correlation heatmap."
        )
        return
    plt.figure(figsize=(10, 8))
    sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm"
    )
    plt.title("Correlation Heatmap")
    plots_folder = Path("output/plots")
    plots_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    plt.savefig(
        plots_folder / "correlation_heatmap.png"
    )
    plt.close()