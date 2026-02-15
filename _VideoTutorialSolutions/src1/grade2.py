# Demonstrates chained comparisons
#
# EXPLANATION:
# Python supports "chained comparisons" - a special feature not in most languages!
#
# KEY CONCEPTS:
# - 90 <= score <= 100 is a chained comparison
# - Python reads this as: 90 <= score AND score <= 100
# - This is unique to Python - most languages don't support this syntax
# - It's more readable and closer to mathematical notation
#
# HOW IT WORKS:
# 1. User enters 95
# 2. Python evaluates: Is 90 <= 95 <= 100?
# 3. This means: Is 90 <= 95? (Yes) AND Is 95 <= 100? (Yes)
# 4. Both are True, so "Grade: A" is printed
#
# CHAINED COMPARISON EXAMPLES:
# - 1 < x < 10 : Is x between 1 and 10 (exclusive)?
# - 0 <= y <= 100 : Is y between 0 and 100 (inclusive)?
# - a < b < c < d : Are these in ascending order?
#
# WHY THIS IS COOL:
# In math, we write: 90 ≤ score ≤ 100
# Python lets us write almost the same thing!
# In languages like C or Java, you must write:
#   score >= 90 && score <= 100

score = int(input("Score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
