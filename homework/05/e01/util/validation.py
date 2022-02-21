import re

'''
function that checks if given date is valid
'''
def is_date(date):
    if not isinstance(date, (str)):
        '''
        if date is not string exception is raised
        '''
        raise Exception("The date you gave was not in correct form, please use YYYY-MM-DD")
    try:
        '''
        first splits given string to parts
        '''
        y_m_d = re.split("-", date)
        year = re.search("^[0-9]{4}$", y_m_d[0])
        month = y_m_d[1]
        day = y_m_d[2]

        '''
        if given date and month are within normal range they are accepted
        year is valid as long as it's 4 numbers
        '''
        for i in range(1, 13):
            if i == int(month):
                month = True
        for i in range(1, 32):
            if i == int(day):
                day = True
        if bool(year) == True and month == True and day == True:
            return True
        else:
            return False
    except:
        raise Exception("The date you gave was not in correct form, please use YYYY-MM-DD")
