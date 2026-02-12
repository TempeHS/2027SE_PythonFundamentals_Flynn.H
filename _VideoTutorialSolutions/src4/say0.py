# Demonstrates pip-installed package
#
# EXPLANATION:
# This program uses 'cowsay', a fun third-party package!
#
# KEY CONCEPTS:
# - Third-party packages are installed using pip (Python's package manager)
# - cowsay makes ASCII art animals "say" messages
# - To install: pip install cowsay
# - Then import and use just like built-in modules
#
# HOW IT WORKS:
# 1. Check if a name was provided
# 2. cowsay.cow() creates an ASCII cow saying the message
#
# OUTPUT EXAMPLE:
#  _______________
# | hello, David |
#  ---------------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||
#
# PIP (Package Installer for Python):
# - pip install package_name - install a package
# - pip uninstall package_name - remove a package
# - pip list - show installed packages
# - pip freeze - show installed packages with versions
#
# PYPI (Python Package Index):
# Thousands of packages at https://pypi.org/
# From web frameworks to data science to games!

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
