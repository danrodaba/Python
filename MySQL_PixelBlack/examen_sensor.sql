create database sensor;
use sensor;

create table T_sensor (
	Row_ID int auto_increment primary key,
    Tipo char(250) not null,
    Estado boolean
    );

insert into T_sensor (Tipo, Estado)
values('Temperatura', True),
	('Humedad', True),
    ('Humedad tierra',False),
    ('Intensidad luminosa',True);

create table T_sensor_audit (
	Row_ID int auto_increment primary key,
    Sensor_ID int not null,
    Estado boolean,
    Valor int,
    Fecha datetime not null,
    Tipo char(250) default 'Lectura',
    foreign key(Sensor_ID) references T_sensor(Row_ID)
    );

insert into T_sensor_audit (Sensor_ID, Estado, Valor, Fecha)
values(1,True,24,'2016-12-09 12:30:05'),
	(2,True,50,'2016-12-10 12:30:05'),
    (3,False,null,'2016-12-11 12:30:05'),
    (4,True,120,'2016-12-12 12:30:05'),
    (1,True,26,'2016-12-13 12:30:10'),
    (2,False,null,'2016-12-14 12:30:10'),
    (3,False,null, '2016-12-15 12:30:10'),
    (4,True,120,'2016-12-16 12:30:10'),
    (1,True,25,'2016-12-17 12:30:15');