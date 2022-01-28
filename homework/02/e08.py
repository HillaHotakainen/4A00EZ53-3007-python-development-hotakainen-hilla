
from multiprocessing.sharedctypes import Value


def get_int(ask, int1, int2):
    nro = 0
    while nro == 0:
        print(ask, "between 4 and 10")
        temp = int(input())
        if temp >= int1 and temp <= int2:
            nro = temp
    return nro

grade = get_int("Give grade", 4, 10)
print("You gave", grade)