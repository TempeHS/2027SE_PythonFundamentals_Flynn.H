# Demonstrates indexing into a list
#
# EXPLANATION:
# This program introduces LISTS - ordered collections of items.
#
# KEY CONCEPTS:
# - A list is created with square brackets: ["item1", "item2", "item3"]
# - Each item has an INDEX (position), starting at 0
# - Access items using: list_name[index]
# - students[0] is "Hermione" (first item, index 0)
# - students[1] is "Harry" (second item, index 1)
# - students[2] is "Ron" (third item, index 2)
#
# WHY START AT 0?
# Most programming languages use "zero-based indexing."
# The first item is at position 0, not 1.
# This is a convention you'll use throughout programming!
#
# INDEX ERRORS:
# students[3] would cause an IndexError - there's no fourth item!
# Always make sure your index is within range.
#
# NEGATIVE INDICES:
# Python also supports negative indices:
# - students[-1] is "Ron" (last item)
# - students[-2] is "Harry" (second to last)
#
# THE PROBLEM HERE:
# This approach doesn't scale. What if there were 100 students?
# See hogwarts1.py for a better approach using loops!

students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])
