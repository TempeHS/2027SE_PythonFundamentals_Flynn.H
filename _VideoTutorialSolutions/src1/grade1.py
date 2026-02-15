# Demonstrates inequalities and logical operators
#
# EXPLANATION:
# This program shows an alternative way to write range comparisons.
#
# KEY CONCEPTS:
# - 90 <= score and score <= 100 is the same as score >= 90 and score <= 100
# - Some programmers find this style more readable
# - It reads like "90 is less than or equal to score, and score is less than or equal to 100"
# - This style mimics mathematical notation: 90 ≤ score ≤ 100
#
# HOW IT WORKS:
# Same logic as grade0.py, just written in a different order.
# The comparison operators are reversed but the meaning is identical.
#
# READABILITY TIP:
# Write code in the style that makes the most sense to you and your team.
# Both styles are correct - choose what's clearest.
#
# MATHEMATICAL COMPARISON:
# In math, we write: 90 ≤ score ≤ 100
# This looks like: 90 <= score <= 100
# Python actually supports this! See grade2.py for "chained comparisons."

score = int(input("Score: "))

if 90 <= score and score <= 100:
    print("Grade: A")
elif 80 <= score and score < 90:
    print("Grade: B")
elif 70 <= score and score < 80:
    print("Grade: C")
elif 60 <= score and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
