def main():
    greeting = input("enter a greeting: ").strip()
    money = money_owed(greeting)
    print(f"you get: {money}")


def money_owed(greeting):
    if greeting.startswith("hello"):
        money = "$0"
    elif greeting.startswith("h"):
        money = "$20"
    else:
        money = "$100"
    return money


if __name__ == "__main__":
    main()
