def main():
    while True:
        try:
            fraction = input("Enter fraction: ")
            x, y = fraction.split("/")
            percent = get_percent(x, y)

            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(percent)
        except (ValueError, ZeroDivisionError):
            print("Please enter a valid fraction: ")
        else:
            break


def get_percent(x, y):
    x = float(x)
    y = float(y)
    percent = round((x / y) * 100)
    return percent


if __name__ == "__main__":
    main()
