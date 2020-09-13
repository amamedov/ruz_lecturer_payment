import ruz
import datetime

lecturers = {}

for x in ruz.lecturers():
    if x['email'] == '':
        lecturers[x['fio']] = x['fio']
    elif x['email'] is None:
        lecturers[x['fio']] = x['fio']
    else:
        lecturers[x['email']] = x['fio']

with open(f'lecturers_in_ruz_{datetime.datetime.today().date()}.txt', 'w') as f:
    for person in lecturers:
        f.write(f'{person}:{lecturers[person]}\n')
