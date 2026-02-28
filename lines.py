import sys


def main():
    file = sys.argv[1]
    file = file_check(file)
    with open(file) as file:
        lines = file.readlines()
    nlines = number_lines(lines)
    print(f"number of lines = {nlines}")


def number_lines(lines):
    count = 0

    for line in lines:
        line_s = line.strip()
        if line_s != "" and not line_s.startswith("#"):
            count += 1

    return count


def file_check(file):
    if file.endswith(".py"):
        return file
    else:
        sys.exit()


main()
