# Absorbance and Reflectance Analysis

## Overview

This project is designed to read absorbance and reflectance data from Excel files, process the data, and plot it using `matplotlib`. The script provides a visual representation of how absorbance and reflectance vary with wavelength, useful for analyzing material properties over a specified wavelength range.

## Features

- Load absorbance and reflectance data from Excel files.
- Clean and filter data based on a specified wavelength range.
- Plot absorbance and reflectance data with interactive cursors.
- Display subplots for easy comparison of absorbance and reflectance.

## Requirements

- Python 3.x
- pandas
- matplotlib
- openpyxl (for reading Excel files)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/absorbance-reflectance-analysis.git
   cd absorbance-reflectance-analysis
   ```

2. **Install the required Python packages:**
   ```bash
   pip install pandas matplotlib openpyxl
   ```

3. **Place your Excel files in the `data` directory:**
   - `data/200-1000_Absorbance.xlsx`
   - `data/200-1000_Reflectance.xlsx`

## Usage

1. **Run the script:**
   ```bash
   python analyze_data.py
   ```

2. **View the plots:**
   - The script will generate and display two subplots: one for absorbance and one for reflectance, both against wavelength.

## Script Explanation

### Importing Libraries
```python
from matplotlib.widgets import Cursor
import pandas as pd
import matplotlib.pyplot as plt
```
- **Cursor**: Creates a crosshair cursor on the plots.
- **pandas**: For data manipulation and analysis.
- **matplotlib.pyplot**: For plotting data.

### Defining Constants
```python
LOWER_LIMIT, UPPER_LIMIT = 200, 1000
```
- Define the wavelength range for filtering the data.

### Loading Data
```python
df_absorbance = pd.read_excel("data/200-1000_Absorbance.xlsx")
df_reflectance = pd.read_excel("data/200-1000_Reflectance.xlsx")
```
- Load data from the specified Excel files.

### Cleaning and Filtering Data
```python
df_absorbance = df_absorbance.dropna().loc[
    (df_absorbance["Wavelength/ nm"] >= LOWER_LIMIT) & (df_absorbance["Wavelength/ nm"] <= UPPER_LIMIT)
]
df_reflectance = (
    df_reflectance.drop(columns=df_reflectance.columns[4:])
    .dropna()
    .loc[(df_reflectance["Wavelength/ nm"] >= LOWER_LIMIT) & (df_reflectance["Wavelength/ nm"] <= UPPER_LIMIT)]
)
```
- Remove rows with missing values and filter data within the specified wavelength range.

### Plotting Data
```python
plt.figure(figsize=(13, 6))
```
- Create a new figure with a specified size.

#### Absorbance Plot
```python
ax_absorbance = plt.subplot(1, 2, 1)
ax_absorbance.plot(df_absorbance["Wavelength/ nm"], df_absorbance.iloc[:, 1:4], label=df_absorbance.columns[1:])
ax_absorbance.set_xlabel("Wavelength (nm)")
ax_absorbance.set_ylabel("Absorbance (%)")
ax_absorbance.set_title("Absorbance vs Wavelength")
ax_absorbance.legend()
cursor_absorbance = Cursor(ax_absorbance, color="k", linewidth=1)
ax_absorbance.grid()
```
- Create a subplot for absorbance data with labels, title, legend, cursor, and grid.

#### Reflectance Plot
```python
ax_reflectance = plt.subplot(1, 2, 2)
ax_reflectance.plot(df_reflectance["Wavelength/ nm"], df_reflectance.iloc[:, 1:4], label=df_reflectance.columns[1:])
ax_reflectance.set_xlabel("Wavelength (nm)")
ax_reflectance.set_ylabel("Reflectance (%)")
ax_reflectance.set_title("Reflectance vs Wavelength")
ax_reflectance.legend()
cursor_reflectance = Cursor(ax_reflectance, color="k", linewidth=1)
ax_reflectance.grid()
plt.tight_layout()
plt.show()
```
- Create a subplot for reflectance data with labels, title, legend, cursor, and grid.
- Use `plt.tight_layout()` to adjust subplots to fit into the figure area without overlapping.
- Display the plots using `plt.show()`.

## Acknowledgements

- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [openpyxl](https://openpyxl.readthedocs.io/)
