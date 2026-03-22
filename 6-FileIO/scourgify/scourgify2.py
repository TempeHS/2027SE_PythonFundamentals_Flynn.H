import sys
import csv


def main():
    file_r = sys.argv[0]
    file_w = sys.argv[1]
    with open(file_r, "r") as infile, open(file_w, 'w') as outfile::
        reader = csv.dictreader(infile)
        writer = csv.dictwriter(outfile)
    for row in reader:
        last, first = row["name"].split(",")
        house = row["house"]
        writer.writerow( {"first": first.strip()
                        "last": last.strip()
                        "house": house.strip())}
                        


if __name__ == "__main__":
    main()
