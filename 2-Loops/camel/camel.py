
def main():
    camelCase = input("Enter camelCase: ")
    snakecase = snake_case(camelCase)
    print(snakecase)


def snake_case(camelCase):

    snake = ""
    for char in camelCase:
        if char.isupper():
            snake = snake + "_" + char.lower()
        else:
            snake = snake + char
    return snake


main()

