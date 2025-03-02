<img src="https://github.com/AshishRogannagari/SheetBuddy/assets/125127793/4c3ecb06-e2c9-4fe4-b79f-3d69c8bf9987" alt="SheetBuddy Logo" width="100%">

# 📌 SheetBuddy: Effortless Data Exploration & Reporting  

[![PyPI - Downloads](https://static.pepy.tech/badge/sheetbuddy)](https://pepy.tech/projects/sheetbuddy)
[![PyPI - Version](https://img.shields.io/pypi/v/sheetbuddy)](https://pypi.org/project/sheetbuddy/)
[![Python Versions](https://img.shields.io/pypi/pyversions/sheetbuddy)](https://pypi.org/project/sheetbuddy/)
[![GitHub Issues](https://img.shields.io/github/issues/AshishRogannagari/sheetbuddy)](https://github.com/AshishRogannagari/sheetbuddy/issues)
[![GitHub Stars](https://img.shields.io/github/stars/AshishRogannagari/sheetbuddy)](https://github.com/AshishRogannagari/sheetbuddy/stargazers)

**SheetBuddy** is a Python library that simplifies **Exploratory Data Analysis (EDA)** by generating **detailed insights and reports in Excel format** 📊.  
It supports **CSV, JSON, and API** data sources, making it a must-have for **data analysts, engineers, and scientists**! 🚀  

---

## 🚀 Why Choose SheetBuddy?  
💚 **Instant EDA Reports** – Summary statistics, missing values, and visualizations in one go.  
💚 **Outlier Detection** – Identifies and visualizes outliers using Z-score and IQR methods.  
💚 **Supports Multiple Data Formats** – Works with **CSV, JSON, and API** datasets.  
💚 **Excel Styling & Formatting** – Well structured reports with tables and insights.  
💚 **Correlation & Distribution Visuals** – Includes **heatmaps, histograms, boxplots**, and more.  
💚 **Fast & Lightweight** – Optimized for quick analysis with minimal dependencies.  

---

## 🎯 New in Version 3.1.1  
 **📊 Outlier Detection & Boxplots** – Detect outliers using **Z-score/IQR** and visualize them.  
 **📈 Correlation Heatmaps & Histograms** – Automatic visual insights in EDA reports.  
 **📝 Structured Dataset Summary** – **New ‘Dataset Info’ sheet** in reports for clarity.  
 **🎨 Conditional Formatting** – Makes reports more readable and professional.  

📚 **[Full Documentation Here](https://sheetbuddy.readthedocs.io/en/latest)**  

---

## 🔧 Installation  
Install SheetBuddy with **pip**:  

```bash
pip install sheetbuddy
```

💡 To upgrade to the latest version:  

```bash
pip install sheetbuddy --upgrade 
```

---

## 🚀 Quick Start: Generate an EDA Report in 3 Steps  

### ✅ Example 1: Generate an EDA Report from a CSV (Online Data)
```python
from sheetbuddy import SheetBuddy 

file_path = 'https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv'
output_file = 'eda_report.xlsx'

sb = SheetBuddy(file_path)
sb.generate_eda_report(output_file)
```

---

### ✅ Example 2: Generate an EDA Report from a Local JSON File
```python
from sheetbuddy import SheetBuddy

file_path = 'path/to/your/data.json'
output_file = 'eda_report.xlsx'

sb = SheetBuddy(file_path)
sb.generate_eda_report(output_file)
```

---

### ✅ Example 3: Generate an EDA Report from a Local CSV File
```python
from sheetbuddy import SheetBuddy

file_path = 'your_local_data.csv'
output_file = 'eda_report.xlsx'

sb = SheetBuddy(file_path)
sb.generate_eda_report(output_file)
```

---

## 🛠️ How It Works
🔹 **Step 1:** Load data from CSV, JSON, or API sources.  
🔹 **Step 2:** Perform **automatic EDA**, including summary stats, missing values, and column descriptions.  
🔹 **Step 3:** Generate a **well-structured Excel report** with visual insights, formatting, and detailed analysis.  

---

## 🛋️ Dependencies  
Make sure you have the following dependencies installed (these are installed automatically with SheetBuddy):  

```bash
pandas==1.3.3
requests==2.26.0
openpyxl==3.0.9
tqdm==4.62.3
matplotlib==3.4.3
seaborn==0.11.2
scipy==1.7.1
```

---

## 🤝 Contributing  
We ❤️ contributions! Feel free to:  
💚 Report **bugs** or suggest **new features** via [GitHub Issues](https://github.com/AshishRogannagari/sheetbuddy/issues).  
💚 Submit a **pull request** to enhance functionality.  
💚 Share SheetBuddy and help us grow the community! 🚀  

---

## 📚 License  
**SheetBuddy** is licensed under the **MIT License**. See the [LICENSE](https://github.com/AshishRogannagari/sheetbuddy/blob/main/LICENSE) file for details.  

---

## 🚀 Get Started with SheetBuddy Today!  
Make your **data analysis faster & more insightful**! 🔥  

📌 **[GitHub Repo](https://github.com/AshishRogannagari/SheetBuddy)** | 📺 **[PyPI Package](https://pypi.org/project/sheetbuddy/)**  
## 📊🛠️ Advanced Usage Examples (Customizing the Report Title & Colors) 
```python
sb.generate_eda_report(output_file, title="My Custom Report", theme="dark")
```


## ❓ Frequently Asked Questions (FAQs)

<details>
  <summary>🔍 What is SheetBuddy?</summary>
  <p><strong>Answer:</strong> SheetBuddy is a Python library designed to automate <strong>Exploratory Data Analysis (EDA)</strong>. It generates well-structured reports with statistics, visualizations, and insights directly in Excel format.</p>
</details>

<details>
  <summary>👨‍💻 Who can use SheetBuddy?</summary>
  <p><strong>Answer:</strong> Anyone working with data! It is especially useful for <strong>data analysts, data engineers, data scientists, and students</strong> who want quick insights into datasets.</p>
</details>

<details>
  <summary>📚 What file formats does SheetBuddy support?</summary>
  <p><strong>Answer:</strong> SheetBuddy supports <strong>CSV, JSON, and API-based data sources</strong>. Future updates may include support for SQL databases.</p>
</details>

<details>
  <summary>📊 What kind of analyses does SheetBuddy perform?</summary>
  <p><strong>Answer:</strong> It performs summary statistics, missing value detection, outlier detection, correlation analysis, and generates visualizations like histograms, boxplots, and heatmaps.</p>
</details>

<details>
  <summary>✅ How do I install SheetBuddy?</summary>
  <p><strong>Answer:</strong> Install it using pip: Pip install sheetbuddy </p>
</details>


 📌 Roadmap & Upcoming Features
## 🚀 Roadmap
🟢 **v3.2.0 (Planned)**
- ✅ Support for direct **SQL database connections**
- ✅ Interactive **Jupyter Notebook Support**
- ✅ **Google Sheets Integration** 🎯

---

🖖 **[Back to Top](#top)** ⬆️
