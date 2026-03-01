import csv
import tabulate
import sys


def main():
    try:
        file = sys.argv[1]
    except IndexError:
        sys.exit("Too few command-line arguments")
    if not file.endswith(".csv"):
        sys.exit("Not a CSV file")
    if len(sys.argv) != 2:
        sys.exit("Too many command-line arguments")
    try:
        with open(file) as file:
            reader = csv.reader(file)
            rows = list(reader)
            headers = rows[0]
            data = rows[1:]
    except FileNotFoundError:
        sys.exit("File does not exist")

    tabulated = file_tabulated(headers, data)
    print(tabulated)


def file_tabulated(headers, data):
    tabulated = tabulate.tabulate(data, headers=headers, tablefmt="grid")
    return tabulated


if __name__ == "__main__":
    main()
