import pyodbc


def add_lecturer(email, name, surname, patronymic):
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-1OJ7R9S\SQLEXPRESS;DATABASE=test')
    cursor = connection.cursor()
    cursor.execute('exec Add_lecturer @email='+email+', @name='+name+', @surname='+surname+',@patronymic=' + patronymic)
    connection.close()

def add_payment_period(start_date, end_date, lecure_rate, practice_rate, seminar_rate):
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-1OJ7R9S\SQLEXPRESS;DATABASE=test')
    cursor = connection.cursor()
    cursor.execute('exec Add_payment_period @start_date='+start_date+', @end_date='+end_date+', @lecture_payment_rate='+lecture_rate+',@practice_payment_rate=' + practice_rate+', @seminar_payment_rate=' + seminar_rate)
    connection.close()

def add_stream(faculty, name, year):
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-1OJ7R9S\SQLEXPRESS;DATABASE=test')
    cursor = connection.cursor()
    cursor.execute('exec Add_stream @faculty='+faculty+', @name='+name+', @year='+year)
    connection.close()

def add_study_plan(year, program, streamID):
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-1OJ7R9S\SQLEXPRESS;DATABASE=test')
    cursor = connection.cursor()
    cursor.execute('exec Add_study_plan @year='+year+', @program='+program+', @streamID='+streamID)
    connection.close()
