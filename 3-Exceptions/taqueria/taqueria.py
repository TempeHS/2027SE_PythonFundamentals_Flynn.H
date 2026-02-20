menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def get_price(item):
    if item in menu:
        return menu[item]
    else:
        return 0


def main():
    total = 0

    while True:
        try:
            item = input("enter order: ")
            item = item.title()
            price = get_price(item)
            total = total + price
            if total > 0:
                print("$", total)
        except EOFError:
            print()
            print("Your total is: ", total)
            break


main()
