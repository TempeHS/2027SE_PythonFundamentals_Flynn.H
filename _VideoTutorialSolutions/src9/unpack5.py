# Indexes into a dict
#
# EXPLANATION:
# You can pass dict values to a function.
#
# KEY CONCEPTS:
# - coins["galleons"] accesses dict value
# - Manually passing each value by key
# - Works, but verbose!
#
# THE CALL:
# coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# total(coins["galleons"], coins["sickles"], coins["knuts"])
#
# This works but is tedious.
# Dict keys even match parameter names!
#
# See unpack6.py for UNPACKING with ** operator!


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
