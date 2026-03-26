import csv


def main():
    infilename = "books.csv"
    outfilename = "overdue.txt"
    overdue = read_file(infilename)
    write_file(outfilename, overdue)


def read_file(infilename):

    with open(infilename, "r") as infile:
        overdue = []
        reader = csv.DictReader(infile)
        for row in reader:
            member = row["member"]
            book = row["book"]
            days_borrowed = row["days_borrowed"]
            days_overdue = int(days_borrowed) - 14

            if days_overdue == 1:
                day_word = "day"
            else:
                day_word = "days"
            if int(days_borrowed) > 14:
                fine = days_overdue * 0.5

                overdue.append(
                    f"{member.title()} - {book}: {days_overdue} {day_word} overdue, ${fine} fine"
                )

    return overdue


def write_file(outfilename, overdue):
    with open(outfilename, "w") as outfile:
        for book in overdue:
            outfile.write(book + "\n")


if __name__ == "__main__":
    main()
