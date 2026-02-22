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
            guess = int(input("enter guess: "))

            if guess == number:
                print("You did it!")
                break
            elif guess > number:
                print("Lower!")
            else:
                print("higher!")

        except ValueError:
            print("must be an integer")


def num_check():
    while True:
        n = int(input("enter level "))
        if not n > 0:
            print("number must be more than 0")
        elif n > 0:
            break
    return n


main()
