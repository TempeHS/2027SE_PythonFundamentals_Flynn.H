# Indexes into list
#
# EXPLANATION:
# You can pass list items to a function.
#
# KEY CONCEPTS:
# - coins[0], coins[1], coins[2] accesses items
# - Manually passing each value
# - Works, but verbose!
#
# THE CALL:
# coins = [100, 50, 25]
# total(coins[0], coins[1], coins[2])
#
# This works but is tedious.
# What if the list has 10 items?
#
# See unpack3.py for UNPACKING with * operator!


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")
