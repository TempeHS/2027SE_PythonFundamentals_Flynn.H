# Adds vaults via operator overloading
#
# EXPLANATION:
# OPERATOR OVERLOADING lets you define + for your class!
#
# KEY CONCEPTS:
# - __add__(self, other) defines the + operator
# - 'self' is left operand, 'other' is right operand
# - Returns a new object (doesn't modify originals)
# - Now: potter + weasley works!
#
# HOW __ADD__ WORKS:
# potter + weasley
# Becomes: potter.__add__(weasley)
# - self = potter
# - other = weasley
# - Returns new Vault with combined values
#
# DUNDER METHODS FOR OPERATORS:
# - __add__: +
# - __sub__: -
# - __mul__: *
# - __eq__: ==
# - __lt__: <
# - __gt__: >
#
# ELEGANT CODE:
# Before: total = Vault(g1+g2, s1+s2, k1+k2)
# After:  total = potter + weasley
#
# The + operator now works like it does for numbers!


class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)
