use master;
create database [test];
use [test];
create table Lecturer(
id int identity(1,1) Primary key clustered,
email nvarchar(50) unique not null,
[name] nvarchar(30) NOT NULL,
surname nvarchar(30) not null,
patronymic nvarchar(30) not null);
create table Stream(
id int identity(1,1) primary key clustered,
faculty nvarchar(50) NOT NULL,
[name] nvarchar(50) not null,
[year] int not null);
create table PaymentPeriod(
id int identity(1,1) primary key clustered,
[start_date] date not null,
end_date date not null,
lecture_payment_rate dec not null,
practice_session_payment_rate dec not null,
seminar_payment_rate dec not null);
create table StudyPlan(
id int identity(1,1) primary key clustered,
[year] int not null,
[program] nvarchar(50) not null,
stream_id int not null,
foreign key (stream_id) references Stream(id));
create table Payment(
id int identity(1,1) primary key clustered,
lecturer_id int not null,
payment_period_id int not null,
amount dec not null,
foreign key (lecturer_id) references Lecturer(id),
foreign key (payment_period_id) references PaymentPeriod(id))