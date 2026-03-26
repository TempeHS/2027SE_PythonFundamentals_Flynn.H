def main():
    infilename = input("Enter input file: ")
    outfilename = input("Enter output file: ")
    cw = input("Enter word to find: ")
    w = cw.lower()

    total = find_word(infilename, w)

    with open(outfilename, "w") as outfile:
        outfile.write(f"{cw} = {total}")


def find_word(infilename, w):
    total = 0
    try:
        if not infilename.endswith(".txt"):
            raise FileNotFoundError
        with open(infilename, "r") as infile:
            for row in infile:
                new_row = ""
                for char in row:
                    if char not in "!?.,":
                        new_row = (new_row + char).lower()
                words = new_row.split()
                for word in words:
                    if word == w:
                        total += 1
        return total

    except FileNotFoundError:
        print("File not found")
        return 0


if __name__ == "__main__":
    main()
