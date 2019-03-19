from RomanDate import roman_date
import datetime
date = datetime.datetime.now()
print('')
print(roman_date(date.day, date.month))
print('')
print('')
while True:
    new_date = input('Enter date (DD MM): ')
    if new_date == 'quit':
        break
    day_month = new_date.split(' ')
    try:
        print(roman_date(int(day_month[0]), int(day_month[1])))
    except ValueError:
        print("You big dummy: Please enter an integer")
    except IndexError:
        try:
            print(roman_date(1, int(day_month[0])))
        except KeyError:
            print('You big dummy: There are only 12 months')
    except KeyError:
        print('You big dummy: There are only 12 months')
    print('')
    print('')
