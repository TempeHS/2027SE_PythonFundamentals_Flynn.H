# Returns student as tuple, without unpacking it
#
# EXPLANATION:
# This keeps the tuple as-is and accesses elements by INDEX.
#
# KEY CONCEPTS:
# - Tuples can be accessed like lists: tuple[0], tuple[1]
# - (name, house) is explicitly a tuple with parentheses
# - student[0] = first element, student[1] = second element
#
# COMPARISON:
# Unpacked (student2.py): name, house = get_student()
# Indexed (this file): student = get_student(); student[0], student[1]
#
# PROBLEM WITH INDEXING:
# student[0] and student[1] are unclear.
# Which is the name? Which is the house?
# You have to remember the order!
#
# This is why we often use DICTIONARIES for named access.
# See student6.py for the dictionary approach!
#
# PARENTHESES ARE OPTIONAL:
# return (name, house) is the same as return name, house
# Parentheses make the tuple more explicit.


def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()
