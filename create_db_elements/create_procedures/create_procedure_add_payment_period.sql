create procedure Add_payment_period
	@start_date date
	, @end_date date
	, @lecture_payment_rate dec
	, @practice_payment_rate dec
	, @seminar_practice_rate dec
as
	insert into PaymentPeriod
	values
		(@start_date, @end_date, @lecture_payment_rate, @practice_payment_rate, @seminar_payment_rate);