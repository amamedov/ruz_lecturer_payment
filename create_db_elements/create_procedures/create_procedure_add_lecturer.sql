create procedure Add_lecturer
	 @email nvarchar(50)
	, @name nvarchar(50)
	, @surname nvarchar(50)
	, @patronymic nvarchar(50)
	as 
	insert into Lecturer values (@email, @name, @surname, @patronymic);