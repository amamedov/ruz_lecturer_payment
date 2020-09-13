import model
# import import_data
import ruz
import datetime
import utils

# print(ruz.person_lessons('sefremov@hse.ru'))

lecturer_email = 'sefremov@hse.ru'
# lecturer_email =  str(input('Enter person`s email: '))

start_date = '2020.09.01'
# start_date = str(input('Enter start date of searched period (YYYY.mm.dd): '))

end_date = '2020.09.30'
# end_date =  str(input('Enter end date of searched period (YYYY.mm.dd): '))
print('Please enter numeric values (no check implemented yet)\n')
lecture_payment = 100  # float(input('Enter lecture wage: '))

seminar_payment = 1750  # float(input('Enter seminar wage: '))

practice_payment = 20  # float(input('Enter practice lesson wage: '))

lessons = ruz.person_lessons(lecturer_email, start_date, end_date)

lectures = [x for x in lessons if x['kindOfWork'] == 'Лекция']

seminars = [x for x in lessons if x['kindOfWork'] == 'Семинар']

practice = [x for x in lessons if x['kindOfWork'] == 'Практическое занятие']

subjects = set([x['discipline'] for x in lessons])

if len(lessons) > 0:
    print(f'Person email: {lecturer_email} (TBD: find name using lookups)')
    print(f'{lecture_payment} RUB for lecture\n{seminar_payment} RUB for'
          f' seminar\n{practice_payment} RUB for practice lesson')
    print(
        f'Total payment: '
        f'{len(seminars) * seminar_payment + len(lectures) * lecture_payment + len(practice) * practice_payment} RUB\n')

    print('Detailed report:')

    for subject in subjects:
        print(f'Subject: {subject}')

        # seminars details
        print(f'\tNumber of seminars: {len([x for x in seminars if x["discipline"] == subject])}')
        if len([x for x in seminars if x["discipline"] == subject]) > 0:
            print(
                f'\t\tFirst date: {min([datetime.datetime.strptime(x["date"], "%Y.%m.%d").date() for x in seminars if x["discipline"] == subject])}')
            print(
                f'\t\tLast date: {min([datetime.datetime.strptime(x["date"], "%Y.%m.%d").date() for x in seminars if x["discipline"] == subject])}')

        # lectures details
        print(f'\tNumber of lectures: {len([x for x in lectures if x["discipline"] == subject])}')
        if len([x for x in lectures if x["discipline"] == subject]) > 0:
            print(
                f'\t\tFirst date: {min([datetime.datetime.strptime(x["date"], "%Y.%m.%d").date() for x in lectures if x["discipline"] == subject])}')
            print(
                f'\t\tLast date: {min([datetime.datetime.strptime(x["date"], "%Y.%m.%d").date() for x in lectures if x["discipline"] == subject])}')

        # practice lessons details
        print(f'\tNumber of practice lessons: {len([x for x in practice if x["discipline"] == subject])}')
        if len([x for x in practice if x["discipline"] == subject]) > 0:
            print(
                f'\t\tFirst date: {min([datetime.datetime.strptime(x["date"], "%Y.%m.%d").date() for x in practice if x["discipline"] == subject])}')
            print(
                f'\t\tLast date: {min([datetime.datetime.strptime(x["date"], "%Y.%m.%d").date() for x in practice if x["discipline"] == subject])}')
else:
    print(f'{lecturer_email} has no lessons between {datetime.datetime.strptime(start_date, "%Y.%m.%d").date()} '
          f'and {datetime.datetime.strptime(end_date, "%Y.%m.%d").date()}.\nOr incorrect information is entered')
