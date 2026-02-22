import random


def main():
    while True:
        try:
            n = num_check()
            number = random.randint(1, n)
            break
        except ValueError:
            print("You must enter an integer!")

    while True:
        try:
            while True:
                try:
                    guess = int(input("enter guess: "))
                    break
                except ValueError:
                    print("must be an interger")
            if guess == number:
                print("You did it!")
                break
            elif guess != number:
                raise SyntaxError
        except SyntaxError:
            if guess > number:
                print("Lower!")

            else:
                print("higher")


def num_check():
    while True:
        try:

            n = int(input("enter level "))
            if not n > 0:
                raise SyntaxError
        except SyntaxError:
            print("number must be more than 0")
        if n > 0:
            break
    return n


main()
