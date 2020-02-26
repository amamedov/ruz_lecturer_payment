import model
import datetime as dt

lecturers = [model.Lecturer('sefremov@hse.ru')]
payment_periods = [model.PaymentPeriod(dt.date(2020, 2, 1), dt.date(2020,2,29), 20, 30, 40), model.PaymentPeriod(dt.date(2020, 1, 1), dt.date(2020,1,31), 20, 30, 40)]
payments = []
for lecturer in lecturers:
    for period in payment_periods:
        payments.append(model.Payment(period, lecturer))
for payment in payments:
    print(payment.get_payment())