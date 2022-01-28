def muh_funk():
    print("Hilla")

muh_funk()

def mah_funk(name):
    nimi=name
    return nimi

print(mah_funk("Hilla"))

def output(word, nro):
    return nro * word
print(output("hello", 2))

def get_max(one, two, three):
    while one > two and one > three:
        return one
    while two > one and two > three:
        return two
    while three > two and three > one:
        return three

largest = get_max(5, 2, 4)
print(largest)