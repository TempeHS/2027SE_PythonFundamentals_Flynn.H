import csv
import sys


def main():
    while True:
        logchoice = input(f"| Create Account | Login | exit | \n")
        if logchoice.lower() == "create account":
            create_account()
            print("Account created succesfully!")

        elif logchoice.lower() == "login":
            user = input("Enter user: ")
            password = input("Enter password: ")
            status = login(user, password)
            if status == True:
                print("Logged in successfully!")
                menu(user)
            else:
                print("Invalid credentials")
        elif logchoice.lower() == "exit":
            sys.exit("Goodbye!")


def menu(user):
    while True:
        request = input(
            f"| add task | remove task | complete task | view list | exit | \n"
        ).lower()
        if request == "add task":
            add_task(user)
        elif request == "view list":
            list_t = view_task(user)
            for item in list_t:
                print(
                    f"{item['num']}. {item['name']}, {item['desc']}, {item['status']}"
                )
        elif request == "remove task":
            remove_task(user)
            print("Task removed successfully")
        elif request == "complete task":
            complete_task(user)
        elif request == "exit":
            sys.exit("Goodbye!")


def complete_task(user):
    task_num = input("Enter task number to be completed: ")
    with open(f"{user}tasks.csv", "r") as read, open("temp.csv", "w") as temp:
        reader = csv.DictReader(read)
        writer = csv.DictWriter(temp, fieldnames=("num", "name", "desc", "status"))
        writer.writeheader()
        for row in reader:
            if not row["num"] == task_num:
                writer.writerow(
                    {
                        "num": row["num"],
                        "name": row["name"],
                        "desc": row["desc"],
                        "status": row["status"],
                    }
                )
            elif row["num"] == task_num and row["status"] == "incomplete":

                writer.writerow(
                    {
                        "num": row["num"],
                        "name": row["name"],
                        "desc": row["desc"],
                        "status": "complete",
                    }
                )
            else:
                print("Task is already completed!")

    with open(f"{user}tasks.csv", "w") as write, open("temp.csv", "r") as temp:
        writer = csv.DictWriter(write, fieldnames=("num", "name", "desc", "status"))
        reader = csv.DictReader(temp)
        writer.writeheader()
        for row in reader:

            writer.writerow(
                {
                    "num": row["num"],
                    "name": row["name"],
                    "desc": row["desc"],
                    "status": row["status"],
                }
            )


def remove_task(user):
    task_num = input("Enter task number to be removed: ")
    with open(f"{user}tasks.csv", "r") as read, open("temp.csv", "w") as temp:
        reader = csv.DictReader(read)
        writer = csv.DictWriter(temp, fieldnames=("num", "name", "desc", "status"))
        writer.writeheader()
        for row in reader:
            if not row["num"] == task_num:
                num = row["num"]
                if int(num) > int(task_num):
                    num = int(num) - 1
                writer.writerow(
                    {
                        "num": num,
                        "name": row["name"],
                        "desc": row["desc"],
                        "status": row["status"],
                    }
                )

    with open(f"{user}tasks.csv", "w") as write, open("temp.csv", "r") as temp:
        writer = csv.DictWriter(write, fieldnames=("num", "name", "desc", "status"))
        reader = csv.DictReader(temp)
        writer.writeheader()
        for row in reader:
            writer.writerow(
                {
                    "num": row["num"],
                    "name": row["name"],
                    "desc": row["desc"],
                    "status": row["status"],
                }
            )


def view_task(user):
    task = []
    with open(f"{user}tasks.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            task.append(row)
    return task


def add_task(user):
    with open(f"{user}tasks.csv", "r") as file:
        num_lines = 0
        for row in file:
            if not row == "num,name,desc,status" or "":
                num_lines += 1

    taskname = input("Enter name for task: ")
    task_desc = input("enter task description: ")
    with open(f"{user}tasks.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=("num", "name", "desc", "status"))

        writer.writerow(
            {
                "num": num_lines,
                "name": taskname,
                "desc": task_desc,
                "status": "incomplete",
            }
        )


def create_account():
    username = input("Enter username: ")
    password = input("Enter password; ")
    with open("Details.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=("user", "password"))

        writer.writerow({"user": username, "password": password})
    with open(f"{username}tasks.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=("num", "name", "desc", "status"))
        writer.writeheader()


def login(user, password):

    with open("Details.csv", "r") as file:
        reader = csv.DictReader(file)
        is_valid = False
        for row in reader:
            if user == row["user"]:
                if password == row["password"]:
                    is_valid = True
    return is_valid


if __name__ == "__main__":
    main()
