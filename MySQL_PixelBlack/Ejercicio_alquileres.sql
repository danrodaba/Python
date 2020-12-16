create database Alquiler_coches;
use Alquiler_coches;


create table Distribuidor(
	ID int auto_increment primary key,
    nombre_dist varchar(30) not null,
    Direccion varchar(30) not null,
    Ciudad varchar(30) not null,
    dist_phone varchar(10) not null,
    Website varchar(250)
    );

create table Flota(
	ID int auto_increment primary key,
	Matricula varchar(10) not null,
	Marca Varchar(20),
	Modelo Varchar(20),
	Marca_española boolean not null,
    fecha_compra date not null,
	Precio_dia float not null,
	ID_dist int not null,
    foreign key(ID_dist) references Distribuidor(ID)
    );


create table Alquiler(
	ID int auto_increment primary key,
    ID_mat int not null,
	Fecha_out date not null,
    Fecha_in date not null,
    Usuario varchar(10) not null,
    user_phone varchar(10) not null,
    Observaciones varchar(250),
    foreign key(ID_mat) references flota(ID)
    );

    
insert into distribuidor(nombre_dist,direccion, ciudad, dist_phone,website)
values('FLICK CANARIAS',' AV. ESCALERITAS, 40','LAS PALMAS DE G.C.','928-357211','www.flick.es'),
	('OTAYSA',' C/ SERRANO 23','MADRID','91-4453214','www.otaysa.es'),
	('CANAUTO',' AV. CANARIAS, 44','VECINDARIO','928-344322','www.canauto.es'),
	('TOYOTA CANARIAS','C/ TOMAS MORALES 7','LAS PALMAS DE G.C.','928-354319','www.toyota.com'),
	('AUTOS CASTILLA', 'PASEO CASTELLANA 9','MADRID','91-4429914','www.autos-cast.es');

insert into flota(Matricula, Marca, Modelo, Marca_española,fecha_compra, precio_dia, ID_dist)
values ('GC-4328-CC','OPEL','CORSA',False,'1998/11/2',3500,1),
	 ('M-5423-VB','BMW','635',False,'1999/02/01',8300,2),
	 ('GC-1843-BZ','SEAT','IBIZA',True,'1998/12/19',3600,3),
	 ('GC-9943-CC','TOYOTA','LAND CRUISER',False,'1999/1/4',8000,4),
	 ('M-3451-XD','SEAT','IBIZA',True,'1999/03/02',3150,5),
	 ('GC-6634-CC','MERCEDES','190',False,'1999/01/04',7575,3);
     
insert into alquiler(ID_mat,fecha_out,fecha_in,usuario, user_phone, Observaciones)
values(1,'1999-02-01','1999-02-04','42.500.126','928-234512','Rota una luna'),
	(6,'1999-02-06','1999-02-11','43.235.125','928-511955',null),
	(5,'1999-02-09','1999-02-10','56.432.555','616-542975',null),
	(3,'1999-02-23','1999-02-26','19.235.199','616-653466',null),
	(2,'1999-03-02','1999-03-05','42.500.126','928-234512',null),
	(4,'1999-03-07','1999-03-20','56.432.555','616-542975','Cambiar aceite'),
	(4,'1999-03-25','1999-03-30','42.500.126','928-234512',null),
	(5,'1999-04-01','1999-04-06','44.112.765','606-431955',null),
	(1,'1999-04-04','1999-04-09','23.119.654','928-551987',null),
	(3,'1999-04-30','1999-05-05','44.112.765','606-431955','Motor quemado'),
	(6,'1999-05-16','1999-05-20','56.432.555','616-542975',null),
	(5,'1999-05-30','1999-06-03','19.235.199','616-653466',null),
	(4,'1999-06-05','1999-06-10','19.235.199','616-653466',null),
	(3,'1999-06-11','1999-06-14','56.432.555','616-542975','Llevar a desguace');
