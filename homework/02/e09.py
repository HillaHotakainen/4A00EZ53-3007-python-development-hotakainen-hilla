def reverse(word):
    word_lenght = len(word)
    reversed = ""
    i = 1
    while word_lenght >= i:
        reversed = reversed + word[-(i)]
        i = i + 1
    return reversed

print(reverse("Kalle"))