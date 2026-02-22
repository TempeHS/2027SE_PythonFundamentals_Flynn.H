import random


def get_level():
    while True:
        try:
            level = int(input("enter level (1, 2, or 3): "))

            if level in (1, 2, 3):
                break
            else:
                print("invalid please enter 1, 2 or 3")
        except ValueError:
            print("invalid please enter 1, 2, 3")
    return level


def question_asker(total, level):

    x = generate_integer(level)
    y = generate_integer(level)
    operators = ["+", "-", "*", "/"]
    op = random.choice(operators)
    print(x, op, y)
    if op == "+":
        ans = x + y
    elif op == "-":
        ans = x - y
    elif op == "*":
        ans = x * y
    elif op == "/":
        ans = x / y
        ans = round(ans, 1)
    while True:
        try:
            guess = input("Enter your guess: ")
            guess = float(guess)
            if guess == ans:
                print("Correct!")
                break
            else:
                print("incorrect")
                total = total - 1
                break
        except ValueError:
            print("Please enter an integer")
    return total


def generate_integer(level):

    n = (10**level) - 1
    n = random.randint(1, n)
    return n


def main():
    total = 10
    level = get_level()
    for i in range(10):
        total = question_asker(total, level)
    print("total is", total, "/ 10")


main()
