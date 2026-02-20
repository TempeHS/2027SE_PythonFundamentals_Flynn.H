def main():
    percent = get_int()

    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(percent)


def get_int():
    while True:
        try:
            fraction = input("Enter fraction: ")
            x, y = fraction.split("/")

            x = int(x)
            y = int(y)

            percent = round((x / y) * 100)
        except (ValueError, ZeroDivisionError):
            print("Please enter a valid fraction: ")
        else:
            break
    return percent


main()
