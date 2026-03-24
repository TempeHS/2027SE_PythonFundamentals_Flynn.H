import csv
import sys
from tabulate import tabulate


def main():
    filename = sys.argv[1]
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        tabulated = tabulate(rows, headers="keys", tablefmt="grid")
        print(tabulated)


if __name__ == "__main__":
    main()
