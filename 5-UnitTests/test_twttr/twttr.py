def main():
    text = input("enter your text: ")
    text = shorten_text(text)
    print(text)


def shorten_text(text):

    tweet = ""
    vowels = "AEIOUaeiou"
    for char in text:
        if char not in vowels:
            tweet = tweet + char
    return tweet


if __name__ == "__main__":
    main()
