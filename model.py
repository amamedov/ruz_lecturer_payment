import ruz
import utils


class Lesson:
    def __init__(self, lecturer, date, discipline, discipline_oid, discipline_in_plan, parent_schedule, kind_of_work):
        self.date = date
        self.lecturer = lecturer
        self.discipline = discipline
        self.discipline_oid = discipline_oid
        self.discipline_in_plan = discipline_in_plan
        self.parent_schedule = parent_schedule
        self.kind_of_work = kind_of_work


class Lecturer:
    def __init__(self, email):
        self.email = email


class Stream:
    def __init__(self, name, year, faculty):
        self.faculty = faculty
        self.name = name
        self.year = year


class PaymentPeriod:
    def __init__(self, start_date, end_date, lecture_payment_rate, practice_payment_rate, seminar_payment_rate):
        self.start_date = start_date
        self.end_date = end_date
        self.lecture_payment_rate = lecture_payment_rate
        self.practice_payment_rate = practice_payment_rate
        self.seminar_payment_rate = seminar_payment_rate


class Payment:
    def __init__(self, payment_period, lecturer):
        self.lecturer = Lecturer(lecturer)
        self.payment_period = PaymentPeriod(payment_period)
        self.schedule = ruz.person_lessons(self.lecturer.email, utils.format_date(self.payment_period.start_date),
                                           utils.format_date(self.payment_period.end_date))
        self.amount = 0


class StudyPlan:
    def __init__(self, year, program):
        self.year = year
        self.program = program