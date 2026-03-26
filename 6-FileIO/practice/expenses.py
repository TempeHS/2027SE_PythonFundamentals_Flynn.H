import csv


def main():
    total = {}
    infilename = "expenses.txt"
    outfilename = input("enter outfile: ").strip()
    with open(infilename, "r") as infile, open(outfilename, "w") as outfile:
        reader = csv.DictReader(infile)
        for row in reader:
            name = row["name"]
            amount = float(row["amount"])
            if row["name"] not in total:
                total[name] = amount
            else:
                total[name] = float(total[name]) + float(row["amount"])

        for name in total:
            outfile.write(f"{name.title()}: {total[name]} \n")


if __name__ == "__main__":
    main()
