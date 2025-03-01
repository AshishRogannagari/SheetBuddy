# Configuration file for Sphinx documentation builder.

import os
import sys

# Append the parent directory to Python's path
sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../../src")) 


# Project information
project = 'SheetBuddy'
author = 'Ashish Rogannagari'
release = '3.1.1'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

# HTML output options
html_theme = "sphinx_rtd_theme"
