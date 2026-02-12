# Demonstrates immutability of tuples, removes parentheses
# https://scifi.stackexchange.com/q/105992
#
# EXPLANATION:
# This shows that tuples are IMMUTABLE - they CANNOT be changed!
#
# KEY CONCEPTS:
# - Tuples cannot be modified after creation
# - student[1] = "Ravenclaw" will raise TypeError!
# - This is a FEATURE: data integrity
#
# THE CODE WILL CRASH:
# student = ("Padma", "Gryffindor")  # Tuple
# student[1] = "Ravenclaw"  # TypeError: 'tuple' object does not support item assignment
#
# WHY IMMUTABILITY?
# - Prevents accidental changes
# - Safer for data that shouldn't change
# - Can be used as dictionary keys (unlike lists)
#
# BUT WHAT IF WE NEED TO CHANGE IT?
# Option 1: Create a new tuple
# Option 2: Use a list instead (mutable)
#
# See student5.py for using a list!


def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__ == "__main__":
    main()
