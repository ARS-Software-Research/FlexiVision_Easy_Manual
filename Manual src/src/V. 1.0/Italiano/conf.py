# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FlexiVision Easy'
author = 'Ars Team'
copyright = '2025, Ars Automation'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_copybutton', # Copy button for code blocks  
    'sphinx_design', # Advanced graphic blocks
    'sphinxcontrib.video'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# (Facoltativo) permette direttive tipo .. note:: in Markdown
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# Supporta .md come file sorgente
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

# CSS personalizzato
html_css_files = [
    'custom.css',
]

# Logo configuration - apparirà in alto a sinistra nella sidebar
html_logo = "_static/logo_fv.png"

html_theme_options = {
    "logo": {
        "image_light": "_static/logo_fv.png",
        "image_dark": "_static/logo_fv_black.png",
    },
    "show_navbar_depth": 1,
    "show_prev_next": True,
}

html_js_files = [
    'fix_print.js',
]