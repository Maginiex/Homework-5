print("введите день")

this_day = input()
this_day = int(this_day)
print("введите месяц")

this_month = input()
this_month = int(this_month)
print("введите год")

this_year = input()
this_year = int(this_year)


def is_leap(year,day,month):
    if this_year % 4 == 0:
        return True
    else:
        return False

def date(day,month, year):
    if month > 12:
        print('false')
        return False
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
       if day > 31:
           print("false")
           return False
       else:
           print("true")
           return True
    elif (month == 4 or month == 6 or month == 9 or month == 11 or month == 10):
       if day > 30:
           print("false")
           return False
       else:
           print("true")
           return True
    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        if day > 31:
            print("false")
            return False
        else:
            print("true")
            return True
    if month == 2:
        if is_leap(year,day,month):
            if day > 29:
                print("false")
                return False
        if (is_leap(year,day,month) == False):
                if day > 28:
                    print("false")
                    return False
        else:
            print("true")
            return True
date(this_day, this_month, this_year)