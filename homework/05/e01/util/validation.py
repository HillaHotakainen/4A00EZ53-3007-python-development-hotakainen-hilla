from ast import Return
import re


def is_date(date):
    if not isinstance(date, (str)):
        raise Exception("The date you gave was not in correct form, please use YYYY-MM-DD")
    try:
        y_m_d = re.split("-", date)
        year = re.search("^[0-9]{4}$", y_m_d[0])
        month = y_m_d[1]
        day = y_m_d[2]

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
