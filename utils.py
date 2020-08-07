def format_date(day):
    try:
        if day[5] != '0' and day[8] != '0':
            formatted_date = day.replace('-', '.')
        elif day[5] == '0':
            formatted_date = day[0] + day[1] + day[2] + day[3] + '.' + day[6] + '.' + day[8] + day[9]
        else:
            formatted_date = day[0] + day[1] + day[2] + day[3]+'.' + day[5] + day[6] + '.' + day[9]
        return formatted_date
    except ValueError:
        print('Incorrect date!')
