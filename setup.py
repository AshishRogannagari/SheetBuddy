
### `setup.py`
# This file is used to package the library and upload it to PyPI.
# It contains metadata about the library, such as the name, version, author, and dependencies.
# The `setup()` function is called with the following arguments:
# - `SheetBuddy`: The name of the library.


from setuptools import setup, find_packages

# Load the README file.
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="SheetBuddy",
    version="0.1.0",
    author="Ashishrogannagari",
    author_email="Ashishrogannagari98@gmail.com",
    description="A Python library for performing Basic (EDA) and generating comprehensive reports in Excel format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AshishRogannagari/SheetBuddy",
    project_urls={
        "Bug Tracker": "https://github.com/AshishRogannagari/SheetBuddy/issues",
        "Documentation": "https://github.com/AshishRogannagari/SheetBuddy#readme",
        "Source Code": "https://github.com/AshishRogannagari/SheetBuddy",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "pandas>=1.1.0",
        "requests>=2.24.0",
        "openpyxl>=3.0.0",
        "tqdm>=4.48.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.10",
            "black>=19.10b0",
            "flake8>=3.8.3",
        ],
    },
    entry_points={
        "console_scripts": [
            "sheetbuddy=sheetbuddy.cli:main",
        ],
    },
    keywords="eda, data analysis, excel, reporting",
    license="MIT",
)
