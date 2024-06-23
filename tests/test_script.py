from sheetbuddy import SheetBuddy

# Example usage with a URL to a CSV file
url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv'
output_file_name = 'eda_report.xlsx'

sb = SheetBuddy(url)
sb.generate_eda_report(output_file_name)

print(f"EDA report generated: {output_file_name}")

import sys
import os

# Ensure the src directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from sheetbuddy import SheetBuddy

# Example usage with a URL to a CSV file
url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv'
output_file_name = 'eda_report.xlsx'

sb = SheetBuddy(url)
sb.generate_eda_report(output_file_name)

print(f"EDA report generated: {output_file_name}")
