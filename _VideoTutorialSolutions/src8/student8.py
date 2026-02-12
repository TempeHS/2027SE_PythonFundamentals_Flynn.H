# Demonstrates mutability of dicts
#
# EXPLANATION:
# This shows that dictionaries are MUTABLE - values can be changed!
#
# KEY CONCEPTS:
# - Dicts are mutable like lists
# - student["house"] = "Ravenclaw" changes the value
# - Unlike tuples, dicts can be modified
#
# HOW IT WORKS:
# 1. Get student as a dict
# 2. If name is "Padma", change house to "Ravenclaw"
# 3. Print the (possibly modified) student
#
# DICT MUTABILITY:
# student = {"name": "Padma", "house": "Gryffindor"}
# student["house"] = "Ravenclaw"  # Works!
# Now: {"name": "Padma", "house": "Ravenclaw"}
#
# DICTS VS CLASSES:
# Dicts work, but classes offer more:
# - Methods (functions attached to data)
# - Validation (ensure data is valid)
# - Custom printing
#
# See student9.py for our first CLASS!


def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()
