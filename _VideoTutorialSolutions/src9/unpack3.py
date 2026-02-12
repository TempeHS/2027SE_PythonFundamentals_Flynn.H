# Unpacks a list
#
# EXPLANATION:
# The * operator unpacks a list into arguments!
#
# KEY CONCEPTS:
# - *coins unpacks the list
# - total(*coins) is like total(coins[0], coins[1], coins[2])
# - Much cleaner for passing list items!
#
# THE MAGIC:
# coins = [100, 50, 25]
# total(*coins)  # Unpacks to: total(100, 50, 25)
#
# * OPERATOR:
# - In function call: Unpacks sequence into arguments
# - Must match number of parameters!
#
# COMPARE:
# total(coins[0], coins[1], coins[2])  # Manual
# total(*coins)  # Unpacking - elegant!
#
# See unpack4.py for named arguments!


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(*coins), "Knuts")
