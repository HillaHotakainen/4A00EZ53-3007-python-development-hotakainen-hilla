def read_database():
    f = open("database.txt", "r")
    return f.read()

def save_to_database(fname, lname):
    f = open("database.txt", "r")
    for x in f:
        last_line = (x)
    id_number = int(last_line[0])+1
    result = open("database.txt", "a")
    result.write(f"\n{id_number},{fname},{lname}")

save_to_database("James", "Bond")
print(read_database())