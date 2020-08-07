import pyodbc 
import model


def import_data():
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-1OJ7R9S\\SQLEXPRESS;DATABASE=test')
    cursor = connection.cursor()
    # Create a list of Lecturer objects with data retrieved from database
    lecturers = []
    lecturers_from_db = cursor.execute('select * from Lecturer')
    while True:
        lecturer = lecturers_from_db.fetchone()
        if lecturer is None:
            break
        lecturers.append(model.Lecturer(lecturer[0], lecturer.email, lecturer.name,
                                        lecturer.surname, lecturer.patronymic))
    # Create a list of streams
    streams = []
    streams_from_db = cursor.execute('select * from Stream')
    while True:
        stream = streams_from_db.fetchone()
        if stream is None:
            break
        streams.append(model.Stream(stream.id, stream.name, stream.year, stream.faculty))
    # Create a list of study plans
    study_plans = []
    study_plans_from_db = cursor.execute('select * from StudyPlan')
    while True:
        study_plan = streams_from_db.fetchone()
        if study_plan is None:
            break
        study_plans.append(model.StudyPlan(study_plan.year, study_plan.program,
                                           next(stream for stream in streams if stream.id == study_plan.id)))
    # Create a list of payment periods
    payment_periods = []
    payment_periods_from_db = cursor.execute('select * from PaymentPeriod')
  
    while True:
        payment_period = payment_periods_from_db.fetchone()
        if payment_period is None:
            break
        payment_periods.append(model.PaymentPeriod(payment_period.id, payment_period.start_date, payment_period.end_date
                                                   , payment_period.lecture_payment_rate,
                                                   payment_period.practice_session_payment_rate,
                                                   payment_period.seminar_payment_rate))
    # Create a list of payments
    payments = []
    payments_from_db = cursor.execute('select * from Payment')
    while True:
        payment = payment_periods_from_db.fetchone()
        if payment is None:
            break
        payments.append(model.Payment(next([period for period in payment_periods
                                            if period.id == payment.payment_period_id]),
                                      next([lecturer for lecturer in lecturers if lecturer.id == payment.lecturer_id])))
    connection.close()
    return lecturers, streams, study_plans, payment_periods, payments

