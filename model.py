import ruz
import utils


class Lesson:
    def __init__(self, id, lecturer, date, discipline, discipline_oid, discipline_in_plan, parent_schedule, kind_of_work):
        self.id = id
        self.date = date
        self.lecturer = lecturer
        self.discipline = discipline
        self.discipline_oid = discipline_oid
        self.discipline_in_plan = discipline_in_plan
        self.parent_schedule = parent_schedule
        self.kind_of_work = kind_of_work


class Lecturer:
    def __init__(self, id, email, name, surname, patronymic):
        self.id = id
        self.email = email
        self.name = name
        self.surname = surname
        self.patronymic = patronymic


class Stream:
    def __init__(self, id, name, year, faculty):
        self.id = id
        self.faculty = faculty
        self.name = name
        self.year = year


class PaymentPeriod:
    def __init__(self, id, start_date, end_date, lecture_payment_rate, practice_payment_rate, seminar_payment_rate):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.lecture_payment_rate = lecture_payment_rate
        self.practice_payment_rate = practice_payment_rate
        self.seminar_payment_rate = seminar_payment_rate


class Payment:
    def __init__(self, payment_period: PaymentPeriod, lecturer: Lecturer):
        self.lecturer = lecturer
        self.payment_period = payment_period
        self.schedule = Schedule(payment_period, lecturer)


    def get_payment(self):
        self.amount = 0
        for lesson in self.schedule.lessons:
            if lesson.kind_of_work == 'Лекция':
                self.amount += self.payment_period.lecture_payment_rate
            elif lesson.kind_of_work == 'Семинар':
                self.amount += self.payment_period.seminar_payment_rate
            elif lesson.kind_of_work == 'Практическое занятие':
                self.amount += self.payment_period.practice_payment_rate
        return self.amount


class StudyPlan:
    def __init__(self, year, program, stream:Stream):
        self.year = year
        self.program = program
        self.stream = stream


class Schedule:
	def __init__(self, payment_period: PaymentPeriod, lecturer: Lecturer):
		self.payment_period = payment_period
		self.lecturer = lecturer
		timetable = ruz.person_lessons(lecturer.email, utils.format_date(payment_period.start_date), utils.format_date(payment_period.end_date))
		self.lessons = [Lesson(lecturer.email, item['date'], item['discipline'], item['disciplineOid'],item['disciplineinplan'], item['parentschedule'],item['kindOfWork']) for item in timetable]