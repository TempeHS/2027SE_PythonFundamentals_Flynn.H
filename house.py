name = input("what's your name? ")

match name:
    case "harry" | "hermione" | "ron":
        print("Gryffindor")
    case "draco":
        print("slytherin")
    case _:
        print("who?")
