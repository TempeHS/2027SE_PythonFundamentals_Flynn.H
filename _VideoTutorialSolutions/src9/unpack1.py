# Passes positional arguments as usual
# https://harrypotter.fandom.com/wiki/Wizarding_currency
#
# EXPLANATION:
# Functions can take multiple positional arguments.
#
# KEY CONCEPTS:
# - total(100, 50, 25): Three positional arguments
# - Arguments match parameters by position
# - galleons=100, sickles=50, knuts=25
#
# WIZARD CURRENCY:
# - 1 Galleon = 17 Sickles
# - 1 Sickle = 29 Knuts
# - Formula converts everything to Knuts
#
# THE MATH:
# (galleons * 17 + sickles) * 29 + knuts
# = total value in Knuts
#
# See unpack2.py for passing values from a list!


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(100, 50, 25), "Knuts")
