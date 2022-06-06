num = int(input())


def season(num_month):
    if (num_month == 1 or num_month == 2 or num_month == 12):
        print('Зима')
    if (num_month == 3 or num_month == 4 or num_month == 5):
        print('Весна')
    if (num_month == 6 or num_month == 7 or num_month == 8):
        print('Лето')
        if (num_month == 9 or num_month == 10 or num_month == 11):
            print('Осень')


season(num)
