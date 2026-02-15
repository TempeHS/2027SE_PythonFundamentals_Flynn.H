# Demonstrates fewer comparisons
#
# EXPLANATION:
# This is the cleanest version! It uses the elif structure cleverly.
#
# KEY CONCEPTS:
# - Because we use elif, we only reach each condition if previous ones were False
# - If score >= 90 is False, we know score < 90 when checking the next condition
# - So we don't need to check score < 90 - it's already guaranteed!
# - This is called "implicit bounds" from the elif structure
#
# HOW IT WORKS (for score = 75):
# 1. Is 75 >= 90? No. Move to next elif.
# 2. Is 75 >= 80? No. Move to next elif.
# 3. Is 75 >= 70? Yes! Print "Grade: C"
#
# WHY WE DON'T NEED UPPER BOUNDS:
# When we reach "elif score >= 70", we already know:
# - score < 90 (failed first condition)
# - score < 80 (failed second condition)
# So if score >= 70, it must be between 70 and 79!
#
# THE POWER OF ELIF:
# This version is shorter and just as correct. The elif structure
# provides "implicit" information that we can use to simplify our code.
#
# DESIGN PRINCIPLE:
# Start with the highest threshold and work down. This makes the logic clear.

score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
