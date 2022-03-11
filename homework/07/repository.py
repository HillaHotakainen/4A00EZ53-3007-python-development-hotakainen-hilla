def read_database():
    f = open("database.txt", "r")
    return f.read()

print(read_database())