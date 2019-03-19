def roman_date(day, month_int):
    if month_int == 4 or month_int == 6 or month_int == 9 or month_int == 11:
        hollow = True
        feb = False
    elif month_int == 2:
        hollow = True
        feb = True
    else:
        hollow = False
        feb = False
    if hollow == True or feb == True:
        if day <= 5 and day > 1:
            day_type = "Nones"
        elif day > 5 and day <= 13:
            day_type = "Ides"
        elif day > 13 or day == 1:
            day_type = "Kalends"
    elif hollow == False:
        if day <= 7 and day > 1:
            day_type = "Nones"
        elif day > 7 and day <= 15:
            day_type = "Ides"
        elif day > 15 or day == 1:
            day_type = "Kalends"
    if day_type == "Nones" and hollow == True:
        countdown = 5 - day
        countdown += 1
    elif day_type == "Ides" and hollow == True:
        countdown = 13 - day
        countdown += 1
    elif day_type == "Kalends" and hollow == True and feb == False:
        countdown = 31 - day
        countdown += 1
        if day == 1:
            countdown = 1
    elif day_type == "Kalends" and feb == True:
        countdown = 29 - day
        countdown += 1
        if day == 1:
            countdown = 1
    elif day_type == "Nones" and hollow == False:
        countdown = 7 - day
        countdown += 1
    elif day_type == "Ides" and hollow == False:
        countdown = 15 - day
        countdown += 1
    elif day_type == "Kalends" and hollow == False:
        countdown = 32 - day
        countdown += 1
        if day == 1:
            countdown = 1
    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December',
        13: 'January'
    }
    month = month_int
    if day_type == 'Kalends' and day != 1:
        month += 1
    if countdown == 1:
        outcome = 'On the ' + day_type + " of " + months[month]
    elif countdown == 2:
        outcome = 'A day before the ' + day_type + ' of ' + months[month]
    else:
        outcome = str(countdown) + " days before the " + day_type + ' of ' + months[month]
    return outcome
