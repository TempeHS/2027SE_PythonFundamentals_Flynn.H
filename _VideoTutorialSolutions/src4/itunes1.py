# Demonstrates json
#
# EXPLANATION:
# This program formats JSON nicely for human reading using json.dumps().
#
# KEY CONCEPTS:
# - The 'json' module provides tools for working with JSON data
# - json.dumps() converts a Python object to a formatted JSON string
# - indent=2 makes the output nicely indented for readability
# - This is called "pretty printing"
#
# HOW IT WORKS:
# 1. Get JSON response from iTunes API
# 2. json.dumps(data, indent=2) formats it with 2-space indentation
# 3. Print the nicely formatted output
#
# JSON (JavaScript Object Notation):
# - A common format for exchanging data between systems
# - Looks similar to Python dictionaries and lists
# - Used by most web APIs
#
# RAW VS FORMATTED:
# Raw: {"results": [{"trackName": "Song", "artistName": "Artist"}]}
# Formatted:
# {
#   "results": [
#     {
#       "trackName": "Song",
#       "artistName": "Artist"
#     }
#   ]
# }
#
# The formatted version is much easier to read and understand!

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(json.dumps(response.json(), indent=2))
