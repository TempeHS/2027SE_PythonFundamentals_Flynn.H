import sys
import csv


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments")

    file_r = sys.argv[1]
    file_w = sys.argv[2]

    try:
        with open(file_r) as infile, open(file_w, "w") as outfile:

            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(",")
                house = row["house"]
                writer.writerow(
                    {
                        "first": first.strip(),
                        "last": last.strip(),
                        "house": house.strip(),
                    }
                )
    except FileNotFoundError:
        print("File Invalid!")


if __name__ == "__main__":
    main()
