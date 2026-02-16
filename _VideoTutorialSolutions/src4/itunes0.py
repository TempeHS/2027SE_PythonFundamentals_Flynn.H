# Demonstrates requests
#
# EXPLANATION:
# This program makes an HTTP request to the iTunes API to search for songs!
#
# KEY CONCEPTS:
# - 'requests' is a popular third-party library for making web requests
# - sys.argv contains command-line arguments
# - APIs (Application Programming Interfaces) let programs talk to web services
# - response.json() converts the API response to a Python dictionary
#
# HOW IT WORKS:
# 1. Check if user provided a search term as argument
# 2. Make GET request to iTunes Search API with the search term
# 3. Print the JSON response (as a Python dictionary)
#
# COMMAND-LINE USAGE:
# python itunes0.py weezer
# This searches iTunes for songs by "weezer"
#
# SYS.ARGV EXPLAINED:
# - sys.argv[0] is the script name ("itunes0.py")
# - sys.argv[1] is the first argument (the search term)
# - len(sys.argv) != 2 checks if exactly one argument was provided
#
# THE REQUESTS LIBRARY:
# - requests.get(url) makes an HTTP GET request
# - response.json() parses JSON response into Python dict
# - This is how most web APIs are accessed!
#
# NOTE: You need to install requests first: pip install requests

import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(response.json())
