# Implements sort() with an instance method
#
# EXPLANATION:
# This demonstrates an INSTANCE METHOD - needs an object!
#
# KEY CONCEPTS:
# - Instance method: def sort(self, name)
# - Requires creating an object first: hat = Hat()
# - Called on the object: hat.sort("Harry")
# - 'self' refers to the specific hat object
#
# HOW IT WORKS:
# 1. hat = Hat() creates a Hat object
# 2. __init__ sets self.houses (instance attribute)
# 3. hat.sort("Harry") calls sort on that object
# 4. Method accesses self.houses
#
# INSTANCE ATTRIBUTES:
# self.houses belongs to THIS specific hat.
# Each Hat object has its own houses list.
# (Though here we only create one hat.)
#
# USAGE PATTERN:
# hat = Hat()         # Create instance first
# hat.sort("Harry")   # Then call method
#
# See hat1.py for @classmethod alternative!

import random


class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Harry")
