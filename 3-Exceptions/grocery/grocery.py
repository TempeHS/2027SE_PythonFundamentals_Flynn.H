def main():
    groceries = {}

    try:

        while True:
            item = input("enter item: ")
            item = item.lower().strip()
            if item in groceries:
                groceries[item] = groceries[item] + 1
            else:
                groceries[item] = 1
            print(item, groceries[item])
    except EOFError:
        print("done entering items!")
        items_sorted = sorted(groceries.keys())
        for item in items_sorted:
            count = groceries[item]
            item_title = item.title()
            print(f"{count} {item_title}")


main()
