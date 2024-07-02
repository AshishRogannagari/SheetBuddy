# <a name="top"></a>SheetBuddy

SheetBuddy is a Python library for performing exploratory data analysis (EDA), data summary, and generating comprehensive reports in Excel format. It supports reading data from CSV files, JSON files, and APIs.

[![PyPI - Daily Downloads](https://img.shields.io/pypi/dm/sheetbuddy)](https://pypi.org/project/sheetbuddy/)
[![PyPI - Version](https://img.shields.io/pypi/v/sheetbuddy)](https://pypi.org/project/sheetbuddy/)
[![PyPI - License](https://img.shields.io/pypi/l/sheetbuddy)](https://pypi.org/project/sheetbuddy/)
[![Python Versions](https://img.shields.io/pypi/pyversions/sheetbuddy)](https://pypi.org/project/sheetbuddy/)

[![GitHub issues](https://img.shields.io/github/issues/AshishRogannagari/sheetbuddy)](https://github.com/AshishRogannagari/sheetbuddy/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/AshishRogannagari/sheetbuddy)](https://github.com/AshishRogannagari/sheetbuddy/pulls)
[![GitHub contributors](https://img.shields.io/github/contributors/AshishRogannagari/sheetbuddy)](https://github.com/AshishRogannagari/sheetbuddy/graphs/contributors)
[![GitHub forks](https://img.shields.io/github/forks/AshishRogannagari/sheetbuddy)](https://github.com/AshishRogannagari/sheetbuddy/network/members)
[![GitHub stars](https://img.shields.io/github/stars/AshishRogannagari/sheetbuddy)](https://github.com/AshishRogannagari/sheetbuddy/stargazers)
[![GitHub](https://img.shields.io/github/license/AshishRogannagari/sheetbuddy)](https://github.com/AshishRogannagari/sheetbuddy/blob/main/LICENSE)
[![fork](https://img.shields.io/badge/fork-red)](https://github.com/login?return_to=%2FAshishRogannagari%2FSheetBuddy)

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

## Release Notes for SheetBuddy v2.0.0 🚀

### New Features:

1. **📊 Correlation Matrix Sheet**:
   - Automatically generate and save a correlation matrix for numerical columns in your Excel report. Easily spot relationships and dependencies between variables.

2. **🧮 Basic Mathematics Sheet**:
   - Get essential statistics like mean, median, mode, and range for your numerical data. Now included in a separate sheet for quick insights into data distribution and central tendencies.

#### Python Version Requirements:
- This version of SheetBuddy requires Python 3.7 or higher.

Upgrade now to leverage these powerful new features and make your data analysis even more insightful! 📈✨

## Installation

You can install SheetBuddy using `pip`:

```bash
pip install sheetbuddy
```
# or

```bash
pip install sheetbuddy==2.0.0
```

## Check for the lastest version


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


We hope you enjoy these new features and improvements in SheetBuddy v2.0.0 ! 🚀

<a href="#top" style="position:fixed;bottom:20px;right:20px;background-color:#007bff;color:white;padding:15px 20px;border-radius:25px;text-align:center;text-decoration:none;font-size:18px;box-shadow:2px 2px 5px rgba(0,0,0,0.3);"> Back to Top ↑ </a>










