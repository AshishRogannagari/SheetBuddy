
# SheetBuddy

SheetBuddy is a Python library for performing exploratory data analysis (EDA) , Data sunmmary  and generating comprehensive reports in Excel format. It supports reading data from CSV files, JSON files, and APIs.

![PyPI - Downloads](https://img.shields.io/pypi/dd/sheetbuddy)
![PyPI - Version](https://img.shields.io/pypi/v/sheetbuddy)
![PyPI - License](https://img.shields.io/pypi/l/sheetbuddy)
![Python Versions](https://img.shields.io/pypi/pyversions/sheetbuddy)
![GitHub issues](https://img.shields.io/github/issues/AshishRogannagari/sheetbuddy)
![GitHub pull requests](https://img.shields.io/github/issues-pr/AshishRogannagari/sheetbuddy)
![GitHub contributors](https://img.shields.io/github/contributors/AshishRogannagari/sheetbuddy)
![GitHub forks](https://img.shields.io/github/forks/AshishRogannagari/sheetbuddy)
![GitHub stars](https://img.shields.io/github/stars/AshishRogannagari/sheetbuddy)
![GitHub](https://img.shields.io/github/license/AshishRogannagari/sheetbuddy)



## Features
- Data Cleaning and Preprocessing
- Load data from CSV, JSON, and APIs
- Generate EDA reports in Excel format
- Summary statistics, null values, standard deviation, and more
- Column information including descriptions ('May not be available for all columns')
- Conditional formatting and styling for Excel sheets
- Summary Statistics
- Visualization (Correlation Matrix, Basic Mathematics)
- Data Export (Excel)

## Installation

You can install SheetBuddy using `pip`:

```bash
pip install sheetbuddy==1.0.0
```
# or
```bash
pip install sheetbuddy --upgrade
```

### Usage

Example 1: Generating an  EDA and Datasummary Report from a CSV File.


```python

from sheetbuddy import SheetBuddy 

file_path_or_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv'
output_file_name = 'datasummary_report.xlsx'

sb = SheetBuddy(file_path_or_url)
sb.generate_eda_report(output_file_name)
```



Example 2: Generating an Datasummary & EDA Report from a Local JSON File.

```python

from sheetbuddy import SheetBuddy

file_path = 'path/to/your/data.json'
output_file_name = 'enter_your_desired_name.xlsx'

sb = SheetBuddy(file_path)
sb.generate_eda_report(output_file_name)

```
Example 3: Generating an Datasummary & EDA Report from a Local CSV File.

```python

from sheetbuddy import SheetBuddy

filename = 'your_local_path.csv'
outputfile = 'enter_your_desired_name.xlsx'

sb = SheetBuddy(filename)
sb.generate_eda_report(outputfile)

```
# How It Works:

1.Data Loading: SheetBuddy loads data from the specified source (CSV, JSON, or API).

2.Data Analysis: It performs various data analyses, including summary statistics, null values analysis, and column descriptions.

3.Report Generation: The results are compiled into an Excel file with conditional formatting and styling for easy interpretation.

# Contributing:

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on GitHub.

# License:

SheetBuddy is licensed under the MIT License. See the LICENSE file for more details.
