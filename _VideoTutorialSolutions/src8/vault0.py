# Adds vaults, storing total in new vault
#
# EXPLANATION:
# This manually adds two Vaults together - tedious!
#
# KEY CONCEPTS:
# - Default parameters: galleons=0, sickles=0, knuts=0
# - Multiple attributes per object
# - Manual math to combine vaults
#
# WIZARD MONEY:
# - Galleons: Gold coins (most valuable)
# - Sickles: Silver coins
# - Knuts: Bronze coins
#
# THE PROBLEM:
# To add two vaults, we need:
# galleons = potter.galleons + weasley.galleons
# sickles = potter.sickles + weasley.sickles
# knuts = potter.knuts + weasley.knuts
# total = Vault(galleons, sickles, knuts)
#
# Wouldn't it be nice to just write:
# total = potter + weasley
#
# OPERATOR OVERLOADING can do this!
# See vault1.py for the + operator with __add__!


class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print(total)
