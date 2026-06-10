# ML Preprocessing Assistant

A Python-based tool for loading, analyzing, cleaning, and preprocessing datasets before machine learning training.

## Features

### Dataset Loading
- Load CSV datasets
- File existence validation
- Error handling for invalid file paths

### Dataset Analysis
- Display number of rows and columns
- Display column names
- Display data types
- Analyze missing values
- Analyze duplicate rows

### Data Cleaning
- Remove duplicate rows
- Fill missing numerical values using Median
- Fill missing categorical values using Mode

### Feature Scaling
- StandardScaler
- MinMaxScaler
- Option to skip scaling

### Dataset Export
- Save processed datasets as CSV files

---

## Project Structure

```text
ml-preprocessing-assistant/
│
├── data/
│   └── mpg.csv
│
├── output/
│   └── processed_data.csv
│
├── main.py
├── preprocessing.py
├── utils.py
├── requirements.txt
└── README.md
```

---

## Workflow

```text
Load Dataset
      ↓
Analyze Dataset
      ↓
Clean Dataset
      ↓
Analyze Cleaned Dataset
      ↓
Choose Scaling Method
      ↓
Save Processed Dataset
```

---

## Scaling Options

### StandardScaler

Transforms features to have:

- Mean = 0
- Standard Deviation = 1

Suitable for:
- Logistic Regression
- SVM
- Neural Networks
- PCA

### MinMaxScaler

Transforms features to:

- Range [0, 1]

Suitable for:
- Neural Networks
- Distance-based algorithms
- Bounded features

### Skip Scaling

Keeps original numeric values unchanged.

---

## Example Output

```text
========== Dataset Information ==========

Number of rows: 398
Number of columns: 9

========== Missing Values Analysis ==========

Missing values by column:
- horsepower: 6 missing values

========== Duplicate Analysis ==========

No duplicate rows found in the dataset.

Dataset cleaned successfully!

Scaling applied using standard.

Dataset saved to 'output/processed_data.csv'
```

---

## Technologies Used

- Python
- Pandas
- Scikit-Learn
- Pathlib

---

## Future Improvements

- One-Hot Encoding
- Label Encoding
- Outlier Detection
- Feature Selection Utilities
- Interactive Menu System
- Data Visualization

---

## Learning Objectives

This project was built to practice:

- Data Cleaning
- Missing Value Handling
- Duplicate Detection
- Feature Scaling
- Modular Python Development
- Machine Learning Preprocessing Workflows

---

## Author

Abror Akhmadkhujaev

Machine Learning & AI Engineering Student