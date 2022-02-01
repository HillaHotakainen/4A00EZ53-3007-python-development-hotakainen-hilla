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

def isPalindrome(word, lowercase):
    word_lenght = len(word)
    reversed = ""
    if lowercase==True:
        word = word.casefold()
    i = 1
    while word_lenght >= i:
        reversed = reversed + word[-(i)]
        i = i + 1
    if word == reversed:
        return True
    else:
        return False