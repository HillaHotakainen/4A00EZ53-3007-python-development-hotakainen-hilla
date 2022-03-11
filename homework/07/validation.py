import re

def is_name(name):
        name_check = re.search("^[A-Z|a-z][A-Z|a-z]+$", name)
        result = bool(name_check)
        return result
