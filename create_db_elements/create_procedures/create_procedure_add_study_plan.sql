create procedure Add_study_plan
	@year int
	, @program nvarchar(50)
	, @streamID int
as
	insert into StudyPlan
	values
		(@year, @program, @streamID)