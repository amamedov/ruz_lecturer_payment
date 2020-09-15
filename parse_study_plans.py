import pandas as pd
import os

for file in os.listdir('study_plans'):

    file = 'study_plans\\' + file

    if file.split('.')[-1] == 'xls':

        df = pd.read_excel(file, skiprows=11)

        df = df[['Наименование дисциплины ', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14',
                 'Распределение контактных часов по модулям',
                 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20']]

        df.columns = ['discipline', 'lectures', 'seminars', 'practice', 'module_1', 'module_2', 'module_3', 'module_4']

        df = df.dropna(subset=['lectures', 'seminars', 'practice'], how='all')

        for c in [x for x in df.columns if 'module' in x]:
            df[c] = df[c].apply(pd.isnull)

        df = df.loc[(df.module_1) | (df.module_2) | (df.module_3) | (df.module_4), :]

        df.to_csv(str.join('.', file.split('.')[0:-1]) + '.csv', index=False, sep=';')
