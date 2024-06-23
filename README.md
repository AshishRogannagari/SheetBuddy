# SheetBuddy

SheetBuddy is a powerful Python library designed to perform exploratory data analysis (EDA) and generate comprehensive reports in Excel format. It supports reading data from various sources, including CSV files, JSON files, and APIs, making it a versatile tool for data analysts and data scientists.

## Features

- **Load Data**: Supports loading data from CSV, JSON, and APIs.
- **Generate EDA Reports**: Produces detailed EDA reports in Excel format.
- **Summary Statistics**: Includes summary statistics, null values, standard deviation, and more.
- **Column Information**: Provides descriptions and classifications for columns.
- **Conditional Formatting**: Adds conditional formatting and styling to Excel sheets for better readability.

## Installation

You can install SheetBuddy using `pip`. It is recommended to use a virtual environment to manage dependencies.

### Prerequisites

- Python 3.6 or higher.


SheetBuddy is a Python library for performing exploratory data analysis (EDA) and generating comprehensive reports in Excel format. It supports reading data from CSV files, JSON files, and APIs.

## 🔗 Installation:

You can install SheetBuddy using `pip`:

```bash
pip install sheetbuddy
```
## Usage :



```python
from sheetbuddy import SheetBuddy

file_path_or_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv'
output_file_name = 'eda_report.xlsx'

sb = SheetBuddy(file_path_or_url)
sb.generate_eda_report(output_file_name) 

```


