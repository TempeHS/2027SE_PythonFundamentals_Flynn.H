import csv


def main():
    infilename = "attendance.csv"
    outfilename = "summary.csv"
    with open(outfilename, "w") as file:
        writer = csv.DictWriter(
            file, fieldnames=("name", "present", "absent", "late", "attendance rate")
        )
        writer.writeheader()
    try:
        with open(infilename, "r") as infile:
            present = {}
            absent = {}
            late = {}
            total = []
            reader = csv.DictReader(infile)
            for row in reader:
                name = row["name"]
                attendance = row["status"]

                if name not in total:
                    total.append(name)

                if attendance == "present":
                    if name not in present:
                        present[name] = 1
                    else:
                        present[name] = present[name] + 1
                elif attendance == "absent":
                    if name not in absent:
                        absent[name] = 1
                    else:
                        absent[name] = absent[name] + 1
                elif attendance == "late":
                    if name not in late:
                        late[name] = 1
                    else:
                        late[name] = late[name] + 1

            for name in total:
                file_write(
                    outfilename,
                    name,
                    present,
                    absent,
                    late,
                )
    except FileNotFoundError:
        print("Invalid input file")


def file_write(
    outfilename,
    name,
    present,
    absent,
    late,
):
    if name not in late:
        late[name] = 0

    total_days = int(present[name]) + int(absent[name]) + int(late[name])
    rate = ((int(present[name]) + int(late[name])) / total_days) * 100
    try:
        with open(outfilename, "a") as outfile:
            writer = csv.DictWriter(
                outfile,
                fieldnames=("name", "present", "absent", "late", "attendance rate"),
            )

            writer.writerow(
                {
                    "name": name,
                    "present": present[name],
                    "absent": absent[name],
                    "late": late[name],
                    "attendance rate": rate,
                }
            )
    except FileNotFoundError:
        print("Invalid output file")


if __name__ == "__main__":
    main()
