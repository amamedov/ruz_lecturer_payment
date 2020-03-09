create procedure Add_lecturer
	@id int, @email nvarchar(50)
	, @name nvarchar(50)
	, @surname nvarchar(50)
	, @patronymic nvarchar(50)
	as 
	insert into Lecturer values (@id, @email, @name, @surname, @patronymic);