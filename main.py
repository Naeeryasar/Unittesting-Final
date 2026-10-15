def reverse(string):
    return string[::-1]


def count_vowels(string):
    count = 0

    for l in string:
     if l in "aeiouAEIOU":
            count = count + 1

    return count


def count_words(text):
    if not text:
        return 0
    else:
        return len(text.split())


if __name__ == "__main__":
    print(reverse("Hello world"))
    print(count_vowels("Hello world"))
    print(count_words("Hello world"))

