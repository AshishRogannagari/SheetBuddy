Usage Guide
===========

Here's how to use SheetBuddy:

.. code-block:: python

    from sheetbuddy import SheetBuddy 

    file_path = 'data.csv'
    output_file = 'eda_report.xlsx'

    sb = SheetBuddy(file_path)
    sb.generate_eda_report(output_file)
