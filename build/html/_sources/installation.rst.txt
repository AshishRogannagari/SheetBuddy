Installation Guide
==================

SheetBuddy is available on **PyPI** and can be installed using:

Installation Methods
--------------------

🔹 **Install via `pip`**
   The easiest way to install SheetBuddy is using `pip`:

   .. code-block:: bash

       pip install sheetbuddy

🔹 **Using a Virtual Environment (Recommended)**
   To avoid conflicts with other packages, it is recommended to install SheetBuddy in a virtual environment:

   1. **Create a virtual environment:**

      .. code-block:: bash

          python -m venv sheetbuddy_env

   2. **Activate the virtual environment:**

      - **Windows:**
        
        .. code-block:: bash

            sheetbuddy_env\Scripts\activate  

      - **macOS/Linux:**

        .. code-block:: bash

            source sheetbuddy_env/bin/activate  

   3. **Install SheetBuddy inside the virtual environment:**

      .. code-block:: bash

          pip install sheetbuddy

Verifying Installation
----------------------

After installation, verify that SheetBuddy is installed correctly:

.. code-block:: bash

    python -c "import sheetbuddy; print(sheetbuddy.__version__)"

If you see the installed version number, the installation was successful! 🎉
