import ruz
import datetime

kinds_of_works = [x['name'] for x in ruz.kind_of_works()]

with open(f'kind_of_works_in_ruz_{datetime.datetime.today().date()}.txt', 'w') as f:
    for kind in kinds_of_works:
        f.write(f'{kind}\n')
