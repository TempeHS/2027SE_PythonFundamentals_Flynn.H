months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    date = convert()
    print(date)


def convert():
    
    while True:
        date = input("enter date: ")
        try:
            month, day, year = date.split(" ")
            day = day.replace(",", "")
            day = int(day)
            year = int(year)
            month = month.title()
            if month in months:
                month = months.index(month) + 1
            else:
                month = int(month)
            date = (year, month, day)
            return date
        except ValueError:
            try:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                date = (year, month, day)
                return date
            except ValueError:
                print("please enter either: month day, year or mm/dd/yyyy")


main()
