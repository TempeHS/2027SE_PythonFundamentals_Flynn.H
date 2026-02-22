import inflect


def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("enter name: ")
            names.append(name)
        except EOFError:
            break

    names_formatted = p.join(names)

    print(f"Adieu, adieu, to {names_formatted}")


if __name__ == "__main__":
    main()
