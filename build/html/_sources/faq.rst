Frequently Asked Questions (FAQ)
================================

🔹 **What file formats does SheetBuddy support?**
SheetBuddy can process datasets in the following formats:

- **CSV** (`.csv`)
- **JSON** (`.json`)
- **Excel** (`.xlsx`)
- **API data** (via `requests`)


🔹 **How do I fix `ModuleNotFoundError: No module named 'sheetbuddy'`?**
If you encounter this error, ensure that SheetBuddy is installed correctly:

.. code-block:: bash

    pip install sheetbuddy 

If you're using a **virtual environment**, activate it before running:

.. code-block:: bash

    # Windows
    sheetbuddy_env\Scripts\activate

    # macOS/Linux
    source sheetbuddy_env/bin/activate

    # Then install the package
    pip install --upgrade sheetbuddy


🔹 **Can I use SheetBuddy in Jupyter Notebook?**
Yes! SheetBuddy works perfectly in **Jupyter Notebook**.

.. code-block:: python

    from sheetbuddy import SheetBuddy

    # Load your dataset
    sb = SheetBuddy("data.csv")

    # Generate an EDA report
    sb.generate_eda_report()

📌 **Tip:** If Jupyter Notebook doesn’t detect SheetBuddy, install it inside the notebook:

.. code-block:: python

   pip install sheetbuddy --upgrade


🎯 **Need More Help?**

- Check the **Installation Guide** for setup instructions.

- Visit the **Usage Guide** for examples and advanced features.

🚀 **Enjoy using SheetBuddy!**
