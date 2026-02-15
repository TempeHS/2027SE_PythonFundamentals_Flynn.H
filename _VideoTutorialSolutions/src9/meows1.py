# Demonstrates a class constant
#
# EXPLANATION:
# Constants can belong to a CLASS!
#
# KEY CONCEPTS:
# - MEOWS = 3 inside the class: Class constant
# - Accessed with Cat.MEOWS (class name, not self)
# - Shared by all instances of the class
#
# CLASS VS INSTANCE ATTRIBUTES:
# - Class attribute: Cat.MEOWS (same for all cats)
# - Instance attribute: self.name (per cat)
#
# WHY CLASS CONSTANTS:
# - Keeps related data with the class
# - Clear ownership: "This belongs to Cat"
# - Avoids polluting global namespace
#
# ACCESS PATTERNS:
# Cat.MEOWS    - From anywhere
# self.MEOWS   - Also works inside methods
# (Both refer to the same class constant)


class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()
