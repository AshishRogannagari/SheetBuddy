from setuptools import setup, find_packages

setup(
    name="SheetBuddy",
    version="0.1.2",
    author="Ashish Rogannagari",
    author_email="your_email@example.com",
    description="A library for data summary and analysis from various formats such as CSV, API, URL, etc.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AshishRogannagari/sheetbuddy",  # Replace with your actual GitHub repository URL
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "requests",
        "openpyxl",
        "tqdm",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
