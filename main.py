import model
import datetime as dt
import import_data
import ruz
import utils 

lecturers, streams, study_plans, payment_periods, payments = import_data.import_data()
payments.append(model.Payment(payment_periods[1], lecturers[1]))
for payment in payments:
    print(payment.get_payment())
    print()