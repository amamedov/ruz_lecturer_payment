import model
import datetime as dt
import import_data
import ruz
import utils 

lecturers, streams, study_plans, payment_periods, payments = import_data.import_data()
for payment in payments:
    print(payment.get_payment())
    print()