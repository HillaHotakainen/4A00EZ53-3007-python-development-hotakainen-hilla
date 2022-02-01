def calculate_sum (no1, no2):
    return no1 + no2

def get_max(one, two, three):
    while one > two and one > three:
        return one
    while two > one and two > three:
        return two
    while three > two and three > one:
        return three