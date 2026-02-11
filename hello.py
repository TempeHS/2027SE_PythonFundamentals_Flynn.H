# ask user for their name
name = input("whats your name ").strip().title()

# split users name into firstname and lastname
first, last = name.split(" ")

# say hello to user
print(f"hello, {first}")
