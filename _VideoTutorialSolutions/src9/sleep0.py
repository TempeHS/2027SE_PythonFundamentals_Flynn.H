# Prints n sheep
#
# EXPLANATION:
# A simple program to print increasing rows of sheep!
#
# KEY CONCEPTS:
# - String multiplication: "🐑" * i repeats the emoji
# - range(n): Goes from 0 to n-1
# - Each row has more sheep than the last
#
# OUTPUT FOR n=4:
#          (0 sheep)
# 🐑        (1 sheep)
# 🐑🐑       (2 sheep)
# 🐑🐑🐑      (3 sheep)
#
# Note: First row is empty (0 sheep).
# Helps you fall asleep by counting!
#
# See sleep1.py for adding main()!

n = int(input("What's n? "))
for i in range(n):
    print("🐑" * i)
