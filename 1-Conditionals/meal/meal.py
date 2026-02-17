def main():
    time_str = input("enter time: ")
    time = convert(time_str)

    if 7.0 <= time <= 8.0:
        print("It's breakfast time.")
    elif 12.0 <= time <= 13.0:
        print("It's lunch time.")
    elif 17.0 <= time <= 18.0:
        print("It's dinner time. ")
    else:
        print("It's not time to eat. ")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


main()
