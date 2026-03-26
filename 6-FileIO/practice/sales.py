import csv


def main():
    infilename = "sales.csv"
    outfilename = input("Enter output file: ")
    with open(outfilename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=("name", "total_sales", "commission"))
        writer.writeheader()
    with open(infilename, "r") as infile:
        total = {}
        commission = {}
        reader = csv.DictReader(infile)
        for row in reader:
            name = row["name"]
            department = row["department"]
            sales_amount = row["sales_amount"]

            if name not in total:
                total[name] = int(sales_amount)
            else:
                total[name] = total[name] + int(sales_amount)

            if department == "Electronics":
                commission_amount = int(sales_amount) * 0.10
            elif department == "Furniture":
                commission_amount = int(sales_amount) * 0.08
            else:
                commission_amount = int(sales_amount) * 0.05

            if name not in commission:
                commission[name] = commission_amount
            else:
                commission[name] = commission[name] + commission_amount

        for name in total:
            file_writer(outfilename, total[name], commission[name], name)


def file_writer(outfilename, total, commission, name):
    with open(outfilename, "a") as outfile:
        writer = csv.DictWriter(
            outfile, fieldnames=("name", "total_sales", "commission")
        )

        writer.writerow(
            {
                "name": f"{name}",
                "total_sales": f"{total}",
                "commission": f"{commission}",
            }
        )


if __name__ == "__main__":
    main()
