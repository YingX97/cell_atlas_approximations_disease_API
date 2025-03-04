# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

# Hide the credits warning for atlasapprox-disease
os.environ["ATLASAPPROX_DISEASE_HIDECREDITS"] = "yes"

# -- Project information -----------------------------------------------------

project = 'Cell Atlas Approximations(Disease) API'
copyright = '2025, Fabio Zanini'
author = 'Fabio Zanini, Ying Xu'


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx_tabs.tabs",
    "sphinx.ext.napoleon",
    # "sphinx_gallery.gen_gallery",
]
sphinx_tabs_disable_tab_closing = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for sphinx-gallery ----------------------------------------------
sphinx_gallery_conf = {
    "filename_pattern": "/.*.py",
    "examples_dirs": [
        "../gallery/python",
    ],
    "gallery_dirs": [
        "python/gallery",
    ],
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
# html_static_path = ["_static"]

# -- Enable TODOs in documentation -------------------------------------------
todo_include_todos = True