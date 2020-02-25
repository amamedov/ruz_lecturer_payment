import datetime
import ruz

EMAIL = 0
LECTURES = 1
SEMINARS = 2
PRACTICE = 3


def format_date(day):
    try:
        formatted_date = f'{day.year}.{day.month}.{day.day}'
        return formatted_date
    except ValueError:
        print('Incorrect date!')


def get_schedule_per_period(email, start_date, end_date):
    lectures = []
    practice = []
    seminars = []
    export = ruz.person_lessons(email, format_date(start_date), format_date(end_date))
    for x in export:
        if x['kindOfWork'] == 'Лекция' or x['kindOfWork'] == 'Практическое занятие' or x['kindOfWork'] == 'Семинар':
            item = {'date': x['date'], 'discipline': x['discipline'], 'disciplineOid': x['disciplineOid'],
                    'disciplineinplan': x['disciplineinplan'], 'kindOfWork': x['kindOfWork'],
                    'parentschedule': x['parentschedule']}
            if item['kindOfWork'] == 'Лекция':
                lectures.append(item)
            elif item['kindOfWork'] == 'Практическое занятие':
                practice.append(item)
            elif item['kindOfWork'] == 'Семинар':
                seminars.append(item)
    return [email, lectures, seminars, practice]


def get_payment(schedule, lecture_cost, practice_cost, seminar_cost):
    payment = len(schedule[LECTURES]) * lecture_cost + len(schedule[SEMINARS]) * seminar_cost + \
              len(schedule[PRACTICE]) * practice_cost
    return [schedule[EMAIL], payment]


schedule = get_schedule_per_period('sefremov@hse.ru', datetime.date(2020, 2, 25), datetime.date(2020, 2, 29))
print(schedule[1])
print(schedule[2])
print(schedule[3])
print(get_payment(schedule, 2, 3, 5))
print(len(schedule[PRACTICE]))
