Using SheetBuddy
================

**SheetBuddy** simplifies dataset analysis with an intuitive API.


🔹 **1️⃣ Load a Dataset**
SheetBuddy supports **CSV, JSON, Excel, and API** data sources.

.. code-block:: python

    from sheetbuddy import SheetBuddy

    # Load a CSV file
    sb = SheetBuddy("data.csv")

    # Display summary statistics
    print(sb.get_summary_statistics())


🔹 **2️⃣ Detect Outliers**
Easily identify outliers in your dataset.

.. code-block:: python

    outliers = sb.detect_outliers()
    print(outliers)


🔹 **3️⃣ Generate an EDA Report**
Export an **Excel report** with **data insights and visualizations**.

.. code-block:: python

    sb.generate_eda_report(output_file="eda_report.xlsx")


**Next Steps** 🎯

- Learn more in the **Installation** and **FAQ** sections.

🚀 **Start analyzing your data with SheetBuddy today!**
