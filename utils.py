def format_date(day):
    try:
        formatted_date = f'{day.year}.{day.month}.{day.day}'
        return formatted_date
    except ValueError:
        print('Incorrect date!')
