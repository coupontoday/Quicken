# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Quicken Download Guide'
copyright = '2025, Quicken'
author = 'Quicken Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (add as needed)
extensions = []

# Allow reStructuredText raw HTML
raw_enabled = True

# Templates and patterns to ignore
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (switch to 'sphinx_rtd_theme' if installed, or leave default)
# html_theme = 'sphinx_rtd_theme'

# Basic page info
html_title = "Why Quicken Download is the Smartest Step for Managing Your Finances"
html_short_title = "Quicken Download"
html_favicon = 'favicon.ico'  # Place favicon.ico in _static or root folder

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML in .rst files
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static assets (uncomment if you have them)
# html_static_path = ['_static']
