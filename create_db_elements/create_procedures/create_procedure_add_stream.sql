create procedure Add_stream
	@faculty nvarchar(50)
	, @name nvarchar(50)\
	, @year int
as
	insert into Stream 
	values
		(@faculty, @name, @year);