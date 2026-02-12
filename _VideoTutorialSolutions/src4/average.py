# Demonstrates statistics
#
# EXPLANATION:
# This program shows how to use Python's built-in statistics module.
#
# KEY CONCEPTS:
# - 'import' brings in code from a module (library)
# - Python has many built-in modules for common tasks
# - statistics.mean() calculates the average of a list of numbers
# - Module functions are called with: module_name.function_name()
#
# HOW IT WORKS:
# 1. import statistics - loads the statistics module
# 2. statistics.mean([100, 90]) calculates (100 + 90) / 2 = 95.0
# 3. Prints: 95.0
#
# WHY USE MODULES?
# - Don't reinvent the wheel - use tested, reliable code
# - Modules are collections of related functions
# - Python's standard library has modules for: math, dates, files, etc.
#
# OTHER STATISTICS FUNCTIONS:
# - statistics.median() - middle value
# - statistics.mode() - most common value
# - statistics.stdev() - standard deviation
#
# FINDING MODULES:
# Python has extensive documentation at https://docs.python.org/3/library/
# This lists all built-in modules and their functions.

import statistics

print(statistics.mean([100, 90]))
