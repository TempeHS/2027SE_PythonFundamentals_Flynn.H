# Implements sort() with a class method
#
# EXPLANATION:
# This demonstrates a CLASS METHOD - no object needed!
#
# KEY CONCEPTS:
# - @classmethod decorator makes sort a class method
# - 'houses' is a CLASS ATTRIBUTE (belongs to the class)
# - Call directly on class: Hat.sort("Harry")
# - 'cls' refers to the class, not an instance
#
# CLASS VS INSTANCE ATTRIBUTES:
# - Class attribute: houses = [...] (shared by all)
# - Instance attribute: self.houses = [...] (per object)
# Here, houses belongs to the Hat CLASS itself.
#
# CLASS VS INSTANCE METHODS:
# - Instance method: def sort(self, name) - needs object
# - Class method: def sort(cls, name) - needs class only
#
# USAGE PATTERN:
# Hat.sort("Harry")   # No instance needed!
#
# WHEN TO USE WHICH:
# - Instance method: When you need per-object data
# - Class method: Factory methods, shared operations
#
# There's only one Sorting Hat, so class method works!

import random


class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
