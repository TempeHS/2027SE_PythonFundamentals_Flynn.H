# Returns student as tuple, unpacking it
#
# EXPLANATION:
# This returns BOTH values as a TUPLE and unpacks them!
#
# KEY CONCEPTS:
# - return name, house returns a tuple (name, house)
# - name, house = get_student() unpacks the tuple
# - Tuples are like lists but IMMUTABLE (can't change)
#
# TUPLE:
# A tuple is an ordered, immutable collection.
# Created with: (value1, value2) or just: value1, value2
#
# UNPACKING:
# name, house = ("Harry", "Gryffindor")
# This assigns: name = "Harry", house = "Gryffindor"
#
# WHY TUPLES?
# - Group related data together
# - Immutable = safe from accidental changes
# - Perfect for returning multiple values
#
# See student3.py for accessing tuple elements without unpacking!


def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__ == "__main__":
    main()
