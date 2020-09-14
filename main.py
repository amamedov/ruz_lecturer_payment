import ruz
import datetime
import os
from operator import itemgetter

export_files = os.listdir(r'./ruz_export')

lecturers_files = []
kinds_of_work_files = []

for x in export_files:
    if 'kinds_of_work' in x:
        kinds_of_work_files.append([datetime.datetime.strptime(x.split('.')[0].split('_')[-1], '%Y-%m-%d'), x])
    elif 'lecturers' in x:
        lecturers_files.append([datetime.datetime.strptime(x.split('.')[0].split('_')[-1], '%Y-%m-%d'), x])

lecturers_files.sort(key=itemgetter(0))
kinds_of_work_files.sort(key=itemgetter(0))

latest_lecturers_file = lecturers_files[0][1]
latest_kinds_of_work_file = kinds_of_work_files[0][1]

lecturers = {}
kinds_of_work = []

with open(r'ruz_export/' + latest_lecturers_file, 'r') as  f:
    for row in f.read().split('\n'):
        if row != '':
            lecturers[row.split(':')[0]] = row.split(':')[1]

with open(r'ruz_export/' + latest_kinds_of_work_file, 'r') as f:
    for row in f.read().split('\n'):
        kinds_of_work.append(row)

# lecturer_email = 'sefremov@hse.ru'
lecturer_email = str(input('Enter person`s email: '))

# start_date = '2020.09.01'
start_date = str(input('Enter start date of searched period (YYYY.mm.dd): '))

# end_date = '2020.09.30'
end_date = str(input('Enter end date of searched period (YYYY.mm.dd): '))

print('Please enter numeric values (no check implemented yet)\n')
# lecture_payment = 100
lecture_payment = float(input('Enter lecture wage: '))

# seminar_payment = 1750
seminar_payment = float(input('Enter seminar wage: '))

# practice_payment = 20
practice_payment = float(input('Enter practice lesson wage: '))

lessons = ruz.person_lessons(lecturer_email, start_date, end_date)

lectures = [x for x in lessons if x['kindOfWork'] == 'Лекция']

seminars = [x for x in lessons if x['kindOfWork'] == 'Семинар']

practice = [x for x in lessons if x['kindOfWork'] == 'Практическое занятие']

subjects = set([x['discipline'] for x in lessons])

if len(lessons) > 0:

    if lecturer_email not in lecturers:
        print(f'Person is not present in list of teachers from ruz'
              f' on {latest_lecturers_file.split(".")[0].split("_")[-1]}')
    else:
        print('Teacher:{[x["fio"] for x in ruz.lecturers() if x["email"] == lecturer_email][0]}\n')
    print(f'Email: {lecturer_email}')

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
