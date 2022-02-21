import re

'''
function that checks if email is valid
'''
def is_email(email):
    if not isinstance(email, (str)):
        raise Exception ("Please give a valid e-mail address")
    try:
        '''
        checks all the characters in email and validates it based on it
        '''
        email_check = re.search("^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+[A-Za-z0-9][.][A-Za-z0-9][A-Za-z0-9]+$", email)
        if bool(email_check) == True:
            '''
            if email is valid returns True
            '''
            return True
        else:
            '''
            if email is invalid returns False
            '''
            return False
    except:
        raise Exception("Please give a valid e-mail address")

is_email("jussi.pohjolainen@tuni.co.uk")
is_email("jussi.pohjolainen@tuni.fi")

