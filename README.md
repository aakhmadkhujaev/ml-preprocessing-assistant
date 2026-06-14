# ML Preprocessing Assistant

A Python tool that helps automate common machine learning preprocessing tasks such as data cleaning, encoding, scaling, and visualization.

---

## Features

### Data Analysis

- Analyze missing values
- Analyze duplicate rows
- Display dataset information

### Data Cleaning

- Fill missing values using:
  - Mean
  - Median
  - Mode
- Drop rows with missing values
- Remove duplicate rows

### Data Encoding

- One-Hot Encoding
- Label Encoding
- Skip Encoding

### Feature Scaling

- StandardScaler
- MinMaxScaler
- Skip Scaling

### Data Visualization

- Missing Values Chart
- Histogram for selected numeric columns
- Correlation Heatmap

### Output Files

The project automatically saves:

- `output/cleaned_data.csv`
- `output/processed_data.csv`

Visualization files are saved in:

- `output/plots/missing_values.png`
- `output/plots/*_histogram.png`
- `output/plots/correlation_heatmap.png`

---

## Project Structure

```text
ml-preprocessing-assistant/
│
├── data/
│   └── mpg.csv
│
├── output/
│   ├── cleaned_data.csv
│   ├── processed_data.csv
│   └── plots/
│       ├── missing_values.png
│       ├── horsepower_histogram.png
│       └── correlation_heatmap.png
│
├── main.py
├── preprocessing.py
├── visualization.py
├── utils.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ml-preprocessing-assistant.git
cd ml-preprocessing-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
```

---

## Usage

Run:

```bash
python main.py
```

The application will guide you through:

1. Dataset analysis
2. Visualization options
3. Missing value handling
4. Encoding selection
5. Scaling selection
6. Saving processed datasets

---

## Example Workflow

```text
Load Dataset
      ↓
Analyze Missing Values
      ↓
Analyze Duplicates
      ↓
Visualize Data
      ↓
Clean Dataset
      ↓
Encode Features
      ↓
Scale Features
      ↓
Save Results
```

---

## Example Visualizations

### Missing Values Chart

Shows the number of missing values in each column.

### Histogram

Displays the distribution of a selected numeric feature.

### Correlation Heatmap

Shows relationships between numeric features using correlation coefficients.

---

## Future Improvements

- Box Plots
- Scatter Plots
- Automatic EDA Report Generation
- Pipeline-Based Preprocessing
- Feature Selection Tools

---

## Author

Built as part of a Machine Learning learning journey focused on developing practical data science tools and understanding real-world preprocessing workflows.