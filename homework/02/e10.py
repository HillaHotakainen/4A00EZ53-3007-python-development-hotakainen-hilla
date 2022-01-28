def reverse(word, lowercase):
    word_lenght = len(word)
    reversed = ""
    i = 1
    while word_lenght >= i:
        reversed = reversed + word[-(i)]
        i = i + 1
    if lowercase==True:
        return reversed.casefold()
    else:
        return reversed

print(reverse("Kalle", lowercase=True))
print(reverse("Kalle", lowercase=False))