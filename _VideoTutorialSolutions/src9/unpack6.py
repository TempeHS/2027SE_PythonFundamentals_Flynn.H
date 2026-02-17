# Unpacks a dict
#
# EXPLANATION:
# The ** operator unpacks a dict into named arguments!
#
# KEY CONCEPTS:
# - **coins unpacks the dict
# - Keys become parameter names, values become arguments
# - total(**coins) is like total(galleons=100, sickles=50, knuts=25)
#
# THE MAGIC:
# coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# total(**coins)  # Unpacks to named arguments!
#
# ** OPERATOR:
# - In function call: Unpacks dict into keyword arguments
# - Dict keys must match parameter names!
#
# COMPARE:
# * (single star): Unpacks list/tuple to positional args
# ** (double star): Unpacks dict to keyword args
#
# See unpack7.py for *args and **kwargs!


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")
