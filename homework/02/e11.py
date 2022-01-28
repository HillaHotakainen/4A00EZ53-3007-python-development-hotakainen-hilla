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

print(isPalindrome("Saippuakauppias", lowercase=True))
print(isPalindrome("Saippuakauppias", lowercase=False))
print(isPalindrome("Kalle", lowercase=False))

