Changelog
=========

SheetBuddy follows **Semantic Versioning**. Below are the details for each release.

Version 3.1.1 (Latest) 🚀
--------------------------

📊 **Outlier Detection & Visualization**
   - **Feature:** Detect outliers in numerical columns using **Z-score** or **IQR method**.
   - **Implementation:** New methods `detect_outliers()` and `add_outliers_plot()` to identify and visualize outliers using boxplots.

📈 **Enhanced EDA Visualizations**
   - **Feature:** Comprehensive visualizations in the **EDA sheet**:
     - **Histograms** for numerical columns.
     - **Boxplots** for outliers.
     - **Correlation heatmaps** for understanding relationships.
   - **Implementation:** Integrated methods for automatic visualization in **Excel reports**.

📝 **Custom Text Headings**
   - **Feature:** Descriptive section titles for each visualization.
   - **Implementation:** `add_text_heading()` method for adding custom headings.

📂 **Structured Dataset Summary**
   - **Feature:** New **Dataset Info sheet** providing dataset metadata (format, number of rows, description, and data link).
   - **Implementation:** `add_dataset_info()` method.

📦 **Requirements**
   - `pandas==1.3.3`
   - `requests==2.26.0`
   - `openpyxl==3.0.9`
   - `tqdm==4.62.3`
   - `matplotlib==3.4.3`
   - `seaborn==0.11.2`
   - `scipy==1.7.1`

💾 **Installation**
   - **Requires Python 3.7+**

   .. code-block:: bash

       pip install sheetbuddy==3.1.1
       

📢 **Note**: This library is optimized for **numerical datasets**.

Version 2.0.0 🎯
--------------------------

🔗 **Correlation Matrix Analysis**
   - **Feature:** Computes the correlation matrix for numerical columns.
   - **Benefit:** Helps understand variable relationships.
   - **Output:** Saved as **'Correlation Matrix'** in the generated Excel report.

📊 **Basic Mathematical Statistics**
   - **Feature:** Computes **mean, median, mode, and range**.
   - **Benefit:** Provides an overview of central tendency and dispersion.
   - **Output:** Saved as **'Basic Mathematics'** sheet.

🚀 **Improvements**
   - **Progress Bars:** Enhanced user experience with **loading indicators**.
   - **Better Data Handling:** Optimized for **CSV, JSON, and Excel files**.

🛠️ **Bug Fixes**
   - **Fixed Read-Only File System Errors**: Improved output file handling.
   - **Enhanced Error Logging**: More detailed logs for troubleshooting.

📖 **Documentation**
   - **Expanded Docstrings** for all methods.
   - **New Usage Examples** in the README.

Version 1.0.0 (Initial Release) 🎉
-----------------------------------

📅 **Release Date:** June 23, 2024

🚀 **Major New Features**
   - **Excel Sheet Styling:** Advanced formatting for reports.
   - **Additional Functionalities:** Extended data analysis capabilities.

📈 **Improvements**
   - **Performance Optimization:** Faster execution and larger dataset handling.
   - **Better Data Processing:** Optimized file parsing and encoding.

🛠️ **Bug Fixes**
   - **General Fixes:** Resolved multiple minor issues.
   - **Compatibility Fixes:** Ensured support for different Python & Excel versions.

❌ **Breaking Changes**
   - **API Changes:** Some functions have been renamed.
   - **Deprecated Methods:** Older methods replaced with **more efficient** alternatives.

📖 **Documentation Updates**
   - **New Tutorials** for styling and EDA features.
   - **Example Use Cases:**

.. code-block:: python

    import sheetbuddy as sb

    data = sb.read_csv('data.csv')
    styled_excel = sb.style_excel(data)
    sb.save_excel(styled_excel, 'styled_output.xlsx')

---------------------------

✅ **View Full Changelog on GitHub:**  
🔗 [GitHub Compare View](https://github.com/AshishRogannagari/SheetBuddy/compare/)
