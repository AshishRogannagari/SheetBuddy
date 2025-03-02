Contributing to SheetBuddy
==========================

We ❤️ contributions! Whether it's fixing bugs, adding new features, or improving documentation, **your help is appreciated!**



🔹 **Step 1: Fork & Clone the Repository**
First, fork the **SheetBuddy** repository and clone it to your local machine:

.. code-block:: bash

   git clone https://github.com/AshishRogannagari/SheetBuddy.git
   cd SheetBuddy



🔹 **Step 2: Create a Virtual Environment**
To keep dependencies isolated, create and activate a virtual environment:

.. code-block:: bash

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate

📌 **Tip:** If using **conda**, create an environment with:

.. code-block:: bash

   conda create --name sheetbuddy_env python=3.9
   conda activate sheetbuddy_env



🔹 **Step 3: Install Dependencies**
Now, install **SheetBuddy** in development mode along with documentation dependencies:

.. code-block:: bash

   pip install -e .
   pip install -r docs/requirements.txt



🔹 **Step 4: Make Your Changes**
- Follow best coding practices.  
- Add comments and docstrings for clarity.  
- Ensure your changes **don’t break existing functionality**.  

To check for issues, run:

.. code-block:: bash

   pytest   # If tests are available
   flake8   # To check for linting errors



🔹 **Step 5: Submit a Pull Request (PR)**
Once happy with your changes:

1. **Commit & Push Changes**  

   .. code-block:: bash

      git add .
      git commit -m "Your meaningful commit message"
      git push origin your-branch

2. **Create a Pull Request on GitHub**  

   - Open a PR to **main** branch. 

   - Describe your changes clearly.
     
   - Wait for review & feedback.

🚀 **Thank you for contributing to SheetBuddy!**

We’ll review your PR and get back to you soon. Happy coding! 😊
