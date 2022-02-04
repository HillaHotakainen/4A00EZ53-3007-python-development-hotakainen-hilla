
from os import sep


def is_name(name, ignore_case):
    if name.rfind(" ") == -1:
        return False
    else:
        new_name = name.rsplit(" ")
        first_name = new_name[0]
        last_name = new_name[1]
    if last_name.isalpha() == False or first_name.isalpha() == False:
        return False
    if first_name == first_name.capitalize() and last_name == last_name.capitalize() and len(first_name) > 2 and len(last_name) > 2:
        return True
    elif len(first_name) > 2 and len(last_name) > 2 and ignore_case == True:
        return True
    else:
        return False