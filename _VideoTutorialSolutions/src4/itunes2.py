# Demonstrates iterating over JSON
#
# EXPLANATION:
# This program extracts specific data from the JSON response.
#
# KEY CONCEPTS:
# - JSON responses are converted to Python dicts and lists
# - You can access nested data: o["results"] gets the results list
# - Loop through results to extract specific fields
# - result["trackName"] gets just the song title
#
# HOW IT WORKS:
# 1. Get JSON response and convert to Python object (o)
# 2. o["results"] is a list of song results
# 3. Loop through each result (a dictionary)
# 4. Print just the trackName from each result
#
# JSON STRUCTURE:
# {
#   "results": [
#     {"trackName": "Song 1", "artistName": "Artist 1", ...},
#     {"trackName": "Song 2", "artistName": "Artist 2", ...},
#     ...
#   ]
# }
#
# ACCESSING NESTED DATA:
# - o["results"] - get the list of results
# - o["results"][0] - get the first result
# - o["results"][0]["trackName"] - get the track name of first result
#
# This pattern is common when working with APIs - get the data,
# then navigate through the structure to find what you need.

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&term=" + sys.argv[1]
)
o = response.json()
for result in o["results"]:
    print(result["trackName"])
