import re

def is_email(email):
    if not isinstance(email, (str)):
        raise Exception ("Please give a valid e-mail address")
    try:
        email_check = re.search("^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+[A-Za-z0-9][.][A-Za-z0-9][A-Za-z0-9]+$", email)
        if bool(email_check) == True:
            return True
        else:
            return False
    except:
        raise Exception("Please hurghs")

is_email("jussi.pohjolainen@tuni.co.uk")
is_email("jussi.pohjolainen@tuni.fi")

