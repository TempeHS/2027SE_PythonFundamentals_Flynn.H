# Stores student as (mutable) list
#
# EXPLANATION:
# This uses a LIST instead of a tuple - lists ARE mutable!
#
# KEY CONCEPTS:
# - Lists use [...] instead of (...)
# - Lists CAN be modified after creation
# - student[1] = "Ravenclaw" works now!
#
# COMPARISON:
# Tuple: (name, house) - immutable, can't change
# List: [name, house] - mutable, can change
#
# HOW IT WORKS:
# 1. get_student() returns [name, house] (a list)
# 2. If name is "Padma", change house to "Ravenclaw"
# 3. This works because lists are mutable!
#
# STILL A PROBLEM:
# student[0] and student[1] are still unclear.
# We need NAMED access like student["name"].
#
# See student6.py for dictionaries with named keys!


def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]


if __name__ == "__main__":
    main()
