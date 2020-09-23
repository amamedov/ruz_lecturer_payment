import ruz
import datetime
import os
import pandas as pd
from operator import itemgetter

def load_latest_lookups():
    lecturers = {}
    kinds_of_work = []
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

    with open(r'ruz_export/' + latest_lecturers_file, 'r') as  f:
        for row in f.read().split('\n'):
            if row != '':
                lecturers[row.split(':')[0]] = row.split(':')[1]

    with open(r'ruz_export/' + latest_kinds_of_work_file, 'r') as f:
        for row in f.read().split('\n'):
            kinds_of_work.append(row)
    return lecturers, kinds_of_work


def console_output():
    if len(lessons) > 0:
        if lecturer_email not in lecturers:
            print(f'Person is not present in list of teachers from ruz')
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


lecturers, kinds_of_work = load_latest_lookups()

# lecturer_email = 'sefremov@hse.ru'
lecturer_email = str(input('Enter person`s email: '))

start_date = '2020.09.01'
print('Start date of period: 2020.09.01')
# start_date = str(input('Enter start date of searched period (YYYY.mm.dd): '))

# end_date = '2020.09.30'
end_date = str(input('Enter end date of searched period (YYYY.mm.dd): '))

old_result = pd.DataFrame()
previous_records = [x for x in os.listdir('result') if lecturer_email.split('@')[0] in x]
if len(previous_records) == 0:
    print('Please enter numeric values (no check implemented yet)\n')
    lecture_payment = float(input('Enter lecture wage: '))
    seminar_payment = float(input('Enter seminar wage: '))
    practice_payment = float(input('Enter practice lesson wage: '))
else:
    temp = [('result\\' + x, datetime.datetime.strptime(os.path.splitext(x)[0].split('_')[-1], '%Y.%m.%d')) for x in
            previous_records]
    temp.sort(key=itemgetter(1))
    old_result = pd.read_csv(temp[0][0], sep=';')
    lecture_payment = old_result.lecture_payment.max()
    seminar_payment = old_result.seminar_payment.max()
    practice_payment = old_result.practice_payment.max()

lessons = ruz.person_lessons(lecturer_email, start_date, end_date)
lectures = [x for x in lessons if x['kindOfWork'] == 'Лекция']
seminars = [x for x in lessons if x['kindOfWork'] == 'Семинар']
practice = [x for x in lessons if x['kindOfWork'] == 'Практическое занятие']
subjects = set([x['discipline'] for x in lessons])

# console_output()

total_payment = len(seminars) * seminar_payment + len(lectures) * lecture_payment + len(practice) * practice_payment

result_df = pd.DataFrame(data={'subject': list(subjects)})

result_df['start_date'] = start_date
result_df['end_date'] = end_date
result_df['lecture_payment'] = lecture_payment
result_df['seminar_payment'] = seminar_payment
result_df['practice_payment'] = practice_payment
result_df['lecture_cnt'] = result_df.subject.apply(lambda subject:
                                                   len([x for x in lectures if x["discipline"] == subject]))
result_df['seminar_cnt'] = result_df.subject.apply(lambda subject:
                                                   len([x for x in seminars if x["discipline"] == subject]))
result_df['practice_cnt'] = result_df.subject.apply(lambda subject:
                                                    len([x for x in practice if x["discipline"] == subject]))

result_df['payment'] = result_df.apply(axis=1, func=(lambda x: x.lecture_payment * x.lecture_cnt
                                                               + x.seminar_payment * x.seminar_cnt
                                                               + x.practice_payment * x.practice_cnt))
result_df['is_overpaid'] = 0
result_df['is_overworking'] = 0
if old_result.shape[0] != 0:
    result_df.is_overpaid = result_df.subject.apply(lambda x: 1 if
    result_df.loc[result_df.subject == x, 'payment'].values[0] <
    old_result[old_result.subject == x].payment.values[0]
    else 0)

result_df.sort_values(by='subject').to_csv(f'result\\{lecturer_email.split("@")[0]}_{start_date}_{end_date}.csv',
                                           sep=';', index=False)
