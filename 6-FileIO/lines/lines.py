import sys


def main():
    file = sys.argv[1]
    file = file_check(file)
    with open(file):
        lines = file.readlines()
    nlines = number_lines(lines)
    print(f"number of lines = {count}")


def number_lines(lines):
    count = 0
    line = lines.strip()
    if line != "":
        count = count + 1
    if line != line.startswith("#"):
        count = count + 1
    else:
        count = count + 1
    return count


def file_check(file):
    if file.endswith(".py"):
        return file
    else:
        sys.exit()


main()
