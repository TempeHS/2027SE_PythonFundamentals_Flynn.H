import bcrypt
import csv


def main():
    request = input("| Login | Create account | Exit |").lower()

    if request == "login":
        if login() == True:
            print("Succesfully logged in")
            menu()
        else:
            print("Login failed")
    elif request == "create account":
        create_account()


def menu():
    request = input(f"| Track macros | Track workout | Exit | \n").lower()
    if request == "track macros":
        track_macros()
    elif request == "track workout":
        track_workout()


def login():
    user = input("Enter username: ")
    password = input("Enter password: ")
    with open("trackerDetails.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["user"] == user:
                if row["pass"] == password:
                    return True


def create_account():
    user = input("Enter username: ")
    password = input("Enter password: ")
    with open("trackerDetails.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=("user", "pass"))
        writer.writerow({"user": user, "pass": password})
    print("Account created succesfully")


def track_macros():
    pass


def track_workout():
    pass


if __name__ == "__main__":
    main()
