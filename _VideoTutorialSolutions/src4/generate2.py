# Demonstrates randint
#
# EXPLANATION:
# This program generates a random integer within a range.
#
# KEY CONCEPTS:
# - random.randint(a, b) returns a random integer from a to b (inclusive)
# - "Inclusive" means both a and b are possible results
# - randint(1, 10) can return 1, 2, 3, 4, 5, 6, 7, 8, 9, or 10
#
# HOW IT WORKS:
# 1. random.randint(1, 10) generates a random number from 1 to 10
# 2. Each of the 10 values has an equal chance (10% each)
# 3. The result is printed
#
# EXAMPLES:
# - random.randint(1, 6) - dice roll (1-6)
# - random.randint(1, 100) - random percentage
# - random.randint(0, 255) - random color value (RGB)
#
# RANDINT VS CHOICE:
# - randint: For numeric ranges
# - choice: For picking from a specific list of options
#
# NOTE:
# random.randrange(1, 11) would give the same result.
# randrange is like range - the end is EXCLUSIVE.
# randint includes both endpoints - often more intuitive.

import random

number = random.randint(1, 10)
print(number)
