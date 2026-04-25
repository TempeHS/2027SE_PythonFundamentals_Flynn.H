from datetime import date
import inflect


def main():
    date_ = input("Enter date in format YYYY-MM-DD: ")
    current = find_current()
    total = find_total(date_, current)
    song = convert_to_words(total)
    print(f"minutes since {date_}: {song}")


def find_current():
    return date.today()


def find_total(date_, current):

    year, month, day = date_.split("-")
    dt = date(int(year), int(month), int(day))

    duration = current - dt

    total = duration.total_seconds() / 60
    return total


def convert_to_words(total):
    p = inflect.engine()
    song = p.number_to_words(total, andword="")
    return song


if __name__ == "__main__":
    main()
