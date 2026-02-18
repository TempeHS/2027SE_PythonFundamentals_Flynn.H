total = 0

while total < 50:
    coin = int(input("please enter coin: "))

    if coin in (5, 10, 25):
        total = total + coin
    else:
        print("invalid.")

    if total < 50:
        due = 50 - total
        print(due, "still due")


change = total - 50
print("your change is", change)
