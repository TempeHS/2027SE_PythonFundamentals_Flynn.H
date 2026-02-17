# Modularizes getting student's name and house
#
# EXPLANATION:
# This uses FUNCTIONS to organize the code better.
#
# KEY CONCEPTS:
# - Separate functions for getting name and house
# - Each function has one job (single responsibility)
# - main() coordinates everything
#
# HOW IT WORKS:
# 1. get_name() returns the name
# 2. get_house() returns the house
# 3. main() uses both and prints
#
# STILL A PROBLEM:
# What if we want to return BOTH name and house from one function?
# We can't just return two separate values... or can we?
#
# PYTHON CAN RETURN MULTIPLE VALUES!
# Using tuples: return name, house
#
# See student2.py for returning multiple values!


def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    return input("Name: ")


def get_house():
    return input("House: ")


if __name__ == "__main__":
    main()
