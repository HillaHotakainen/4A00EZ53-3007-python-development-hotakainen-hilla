import re

def is_personal_id(id):
    try:
        ddmmyy = id[0]+id[1]+id[2]+id[3]+id[4]+id[5]
        invid_number = id[7]+id[8]+id[9]
        end_id = id[-1]
        personal_id = re.search("^(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])([0-9][0-9])[+A-](00[2-9]|0[1-9][0-9]|[1-8][0-9][0-9])[0-9A-FHJ-NPR-Y]$", id)
        if bool(personal_id) == True:
            cheking = int(ddmmyy + invid_number)%31
            check_char = "0123456789ABCDEFHJKLMNPRSTUVWXY"
            if check_char[cheking] == end_id:
                return True
        else:
            print ("This was not a valid id")
            return False

    except:
        print("This is not a valid")