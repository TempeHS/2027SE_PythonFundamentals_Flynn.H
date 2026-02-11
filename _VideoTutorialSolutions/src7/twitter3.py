# Allows for http, no protocol, and www.
#
# EXPLANATION:
# This handles many URL variations using optional groups!
#
# KEY CONCEPTS:
# - (...)? makes a group optional
# - https? matches "http" or "https" (s is optional)
# - (https?://)? makes entire protocol optional
#
# PATTERN: r"^(https?://)?(www\.)?twitter\.com/"
# - (https?://)? = optional http:// or https://
# - (www\.)? = optional www.
# - twitter\.com/ = literal twitter.com/
#
# MATCHES:
# - https://twitter.com/user ✓
# - http://twitter.com/user ✓
# - www.twitter.com/user ✓
# - twitter.com/user ✓
# - https://www.twitter.com/user ✓
#
# BREAKING DOWN https?://
# - http = literal "http"
# - s? = optional "s"
# - :// = literal "://"
# Combined: matches "http://" OR "https://"
#
# See twitter4.py for extracting the username with capture groups!

import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")
