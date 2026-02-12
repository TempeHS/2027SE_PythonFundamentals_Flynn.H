# Demonstrates a constant
#
# EXPLANATION:
# CONSTANTS are values that shouldn't change!
#
# KEY CONCEPTS:
# - MEOWS = 3: Uppercase name indicates constant
# - Python doesn't enforce constants - it's a convention
# - Using constants makes code clearer and easier to change
#
# WHY USE CONSTANTS:
# - Magic numbers (like 3) are unclear
# - MEOWS = 3 gives the number meaning
# - Change in one place updates everywhere
#
# NAMING CONVENTION:
# - ALL_CAPS: Indicates constant (don't change!)
# - snake_case: Regular variables
# - PascalCase: Class names
#
# See meows1.py for class constants!

MEOWS = 3

for _ in range(MEOWS):
    print("meow")
