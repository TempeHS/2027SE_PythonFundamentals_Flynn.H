# Eliminates unneeded variable
#
# EXPLANATION:
# This creates the dict in ONE line using literal syntax!
#
# KEY CONCEPTS:
# - {"name": name, "house": house} creates dict directly
# - No need to build up the dict step by step
# - More concise and Pythonic
#
# COMPARISON:
# Verbose (student6.py):
#   student = {}
#   student["name"] = name
#   student["house"] = house
#   return student
#
# Compact (this file):
#   return {"name": name, "house": house}
#
# DICTS ARE GREAT, BUT...
# Dictionaries have limitations:
# - No methods (can't do student.greet())
# - No type checking (any key works)
# - No IDE autocomplete for keys
#
# For more complex data, we use CLASSES!
# See student9.py for our first class!


def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()
