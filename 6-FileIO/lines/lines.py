import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("File not provided")
    elif len(sys.argv) > 2:
        sys.exit("Too many files")
    file = sys.argv[1]
    file = file_check(file)
    try:
        with open(file) as file:
            lines = file.readlines()
        nlines = number_lines(lines)
        print(f"number of lines = {nlines}")
    except FileNotFoundError:
        print("File not found!")


def number_lines(lines):
    count = 0
    for line in lines:
        line = line.strip()
        if line != line.startswith("#") and line != "":
            count += 1
    return count


def file_check(file):
    if file.endswith(".py"):
        return file
    else:
        sys.exit("File Invalid!")


if __name__ == "__main__":
    main()
