def main():
    text = input("enter your text")
    text = vowel_remover(text)
    print(text)


def vowel_remover(text):

    tweet = ""
    vowels = "AEIOUaeiou"
    for char in text:
        if char not in vowels:
            tweet = tweet + char
    return tweet


main()
