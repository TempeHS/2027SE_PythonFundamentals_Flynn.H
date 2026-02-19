def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    if len(plate) < 2 or len(plate) > 6:
        return False
    if not plate[0:2].isalpha():
        return False
    for i in range(len(plate)):
        if plate[i].isdigit():

            if plate[i] == "0":
                return False

            if not plate[i:].isdigit():
                return False

        break

    return True

    if not plate.isalnum():
        return False


main()
