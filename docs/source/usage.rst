Using SheetBuddy
================

SheetBuddy helps in generating EDA reports easily.

### 📌 Example 1: Generate an EDA Report from a CSV

.. code-block:: python

   from sheetbuddy import SheetBuddy

   file_path = "your_data.csv"
   output_file = "eda_report.xlsx"

   sb = SheetBuddy(file_path)
   sb.generate_eda_report(output_file)

### 📌 Example 2: Generate an EDA Report from JSON

.. code-block:: python

   from sheetbuddy import SheetBuddy

   file_path = "your_data.json"
   output_file = "eda_report.xlsx"

   sb = SheetBuddy(file_path)
   sb.generate_eda_report(output_file)

### 📌 Example 3: Customizing Report Title & Theme

.. code-block:: python

   sb.generate_eda_report(output_file, title="My Custom Report", theme="dark")
