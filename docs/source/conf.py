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

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary'
]


# Set the theme
html_title = "SheetBuddy"

html_theme = "sphinx_book_theme"

html_theme_options = {
    "repository_url": "https://github.com/AshishRogannagari/SheetBuddy",
    "use_repository_button": True,
    "use_edit_page_button": False,
    "use_issues_button": True,
    "home_page_in_toc": True,
    "path_to_docs": "docs/source",
    "show_navbar_depth": 2,
}

# Force project name in the sidebar
html_context = {
    "default_mode": "dark",  # Keep dark mode if needed
    "display_github": True,
    "github_user": "AshishRogannagari",
    "github_repo": "SheetBuddy",
    "github_version": "main/docs/",
    "theme_navbar_title": "SheetBuddy",  # This will change the sidebar title
}



