# Demonstrates iterating over a list
#
# EXPLANATION:
# This program shows the Pythonic way to loop through a list.
#
# KEY CONCEPTS:
# - for item in list: iterates over each item in the list
# - The variable 'student' takes on each value in the list, one at a time
# - No need to use indices - Python handles it for you!
# - This is the preferred way to iterate when you just need the values
#
# HOW IT WORKS:
# 1. First iteration: student = "Hermione", print "Hermione"
# 2. Second iteration: student = "Harry", print "Harry"
# 3. Third iteration: student = "Ron", print "Ron"
# 4. No more items, loop ends
#
# READABILITY:
# for student in students:
#     print(student)
#
# This reads almost like English: "for each student in students, print the student"
#
# WHEN TO USE THIS PATTERN:
# - When you need to process each item but don't need the index
# - When the order doesn't matter for your logic
# - When you want the cleanest, most readable code
#
# If you need the index too, see hogwarts2.py!

students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)
