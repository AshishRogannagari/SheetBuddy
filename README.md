
# SheetBuddy

SheetBuddy is a Python library for performing exploratory data analysis (EDA) and generating comprehensive reports in Excel format. It supports reading data from CSV files, JSON files, and APIs.

## Features

- Load data from CSV, JSON, and APIs
- Generate EDA reports in Excel format
- Summary statistics, null values, standard deviation, and more
- Column information including descriptions
- Conditional formatting and styling for Excel sheets

## Installation

You can install SheetBuddy using `pip`:

```bash
pip install sheetbuddy
```

# or

```bash
pip3 install sheetbuddy
```

### Usage

Example 1: Generating an EDA Report from a CSV File.


```python

from sheetbuddy import SheetBuddy 

file_path_or_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv'
output_file_name = 'datasummary_report.xlsx'

sb = SheetBuddy(file_path_or_url)
sb.generate_eda_report(output_file_name)
```



Example 2: Generating an EDA Report from a Local JSON File.

```python

from sheetbuddy import SheetBuddy

file_path = 'path/to/your/data.json'
output_file_name = 'enter_your_desired_name.xlsx'

sb = SheetBuddy(file_path)
sb.generate_eda_report(output_file_name)

```