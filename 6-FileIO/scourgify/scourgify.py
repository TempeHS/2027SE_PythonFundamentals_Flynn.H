import sys
import csv


def main():
    file_r = sys.argv[1]
    file_w = sys.argv[2]
    with open(file_r) as infile, open(file_w, "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(",")
            writer.writerow(
                {
                    "first": first.strip(),
                    "last": last.strip(),
                    "house": row["house"].strip(),
                }
            )


if __name__ == "__main__":
    main()
