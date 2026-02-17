# Adds main
#
# EXPLANATION:
# Wrapping code in main() is a best practice!
#
# KEY CONCEPTS:
# - def main(): contains program logic
# - if __name__ == "__main__": runs main when script executes
# - Prevents code from running when imported as module
#
# WHY USE MAIN():
# - Code is organized in a function
# - Can be imported without running
# - Easier to test and maintain
#
# THE PATTERN:
# def main():
#     ...all program logic...
#
# if __name__ == "__main__":
#     main()
#
# See sleep2.py for extracting a helper function!


def main():
    n = int(input("What's n? "))
    for i in range(n):
        print("🐑" * i)


if __name__ == "__main__":
    main()
