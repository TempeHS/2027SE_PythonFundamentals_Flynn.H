# Appends names to a list for sorting
#
# EXPLANATION:
# This reads from a file and SORTS the names before printing.
#
# KEY CONCEPTS:
# - Read lines into a list so we can sort them
# - Clean each line with rstrip() before adding to list
# - sorted() returns an alphabetically sorted list
#
# HOW IT WORKS:
# 1. Create empty list: names = []
# 2. Read each line from the file
# 3. Clean it with rstrip() and add to list
# 4. Use sorted() to sort alphabetically
# 5. Print each name in order
#
# WHY A LIST?
# To sort, you need all names in memory at once.
# Can't sort a file line-by-line - need the whole list!
#
# ALTERNATIVE (one-liner):
# names = [line.rstrip() for line in file]
# This is a "list comprehension" - same result, more compact.
#
# SORTED VS SORT:
# sorted(list) returns a NEW sorted list
# list.sort() sorts the list in place (modifies original)

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
