# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

"""NOTE: that configuration file is taken directly from discord.py."""

import re


import os
import sys

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "PyTweet"
copyright = "2021, TheGenocide, TheFarGG"
author = "TheGenocide & TheFarGG"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]
autodoc_member_order = "bysource"
autodoc_typehints = "none"
autodoc_inherit_docstrings = False

extlinks = {
    "issue": ("https://github.com/TheFarGG/PyTweet/issues/%s", ""),
    "gh": ("https://github.com/TheFarGG/PyTweet/%s", ""),
    "discord": ("https://discord.com/invite/XHBhg6A4jJ/%s", ""),
}


# Links used for cross-referencing stuff in other documentation
intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
}

# The suffix of source filenames.
source_suffix = ".rst"


# The master toctree document.
master_doc = "index"


version = ""
try:
    with open("../pytweet/__init__.py") as f:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)
except Exception:
    pass

if version:
    release = version

# This assumes a tag is available for final releases
branch = "master" if version.endswith("a") else f"v{version}"

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "obj"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The style name to use for Pygments highlighting of source code.
pygments_style = "friendly"


# -- Options for HTML output -------------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "pytweet.pydoc"

# Output is processed with HTML5 writer. Default is False.
html_experimental_html5_writer = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

html_js_files = []

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []
