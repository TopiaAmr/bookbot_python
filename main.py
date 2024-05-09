def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    print("\n")
    for letter in count_letters(text):
        print(f"The '{list(letter.keys())[0]}' character was found {letter[list(letter.keys())[0]]} times")


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letters = {}
    for letter in text:
        if letter.isalpha():
            if letter.lower() not in letters:
                letters[letter.lower()] = 1
            else:
                letters[letter.lower()] += 1
    lts = []
    for letter in letters:
        lts.append({letter: letters[letter]})
    lts.sort(reverse=True, key=lambda x: x[list(x.keys())[0]])
    return lts


if __name__ == "__main__":
    main()
