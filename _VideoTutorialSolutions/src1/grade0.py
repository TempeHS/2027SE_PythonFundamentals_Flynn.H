# Demonstrates inequalities and logical operators
#
# EXPLANATION:
# This program assigns letter grades based on a numeric score using 'and'.
#
# KEY CONCEPTS:
# - 'and' is a logical operator that requires BOTH conditions to be True
# - score >= 90 and score <= 100 means "between 90 and 100 inclusive"
# - Each elif checks a different score range
#
# HOW IT WORKS:
# 1. User enters a score (e.g., 85)
# 2. Python checks: Is 85 >= 90 AND 85 <= 100? No (85 is not >= 90)
# 3. Python checks: Is 85 >= 80 AND 85 < 90? Yes! Both are true.
# 4. "Grade: B" is printed
#
# UNDERSTANDING 'AND':
# - True and True = True
# - True and False = False
# - False and True = False
# - False and False = False
# Both conditions must be True for 'and' to return True.
#
# SCORE RANGES:
# - 90-100: A
# - 80-89: B
# - 70-79: C
# - 60-69: D
# - Below 60: F
#
# NOTE: This code is a bit verbose. See grade2.py for a cleaner approach.

score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
