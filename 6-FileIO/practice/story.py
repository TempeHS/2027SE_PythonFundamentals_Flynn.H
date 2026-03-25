def main():
    frequency = {}
    infilename = input("Enter infile: ").strip()
    outfilename = input("Enter output file: ").strip()
    while True:
        try:
            with open(infilename, "r") as infile, open(outfilename, "w") as outfile:

                for row in infile:
                    new_row = ""
                    for char in row:
                        if char not in ".,/!?":
                            new_row = new_row + char
                    words = new_row.split()
                    for word in words:
                        word = word.lower()
                        if word not in frequency:
                            frequency[word] = 1
                        elif word in frequency:
                            frequency[word] += 1
                for word in frequency:
                    outfile.write(f"{word.title()}: {frequency[word]} \n")
            break
        except FileNotFoundError:
            infilename = input("Please enter a valid input file: ")


if __name__ == "__main__":
    main()
