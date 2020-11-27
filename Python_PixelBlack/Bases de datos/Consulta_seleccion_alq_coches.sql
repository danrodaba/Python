-- 1. Ver los datos de los alquileres con coches españoles
select * from alquiler inner join flota on ID_mat=flota.ID where Marca_española = True;
-- 2. Ver los datos de los alquileres cuyo precio final exceda de 12000 pts.
select * from alquiler_coches.flota inner join alquiler_coches.alquiler on flota.ID=ID_mat where (fecha_in-fecha_out)*precio_dia>12000; -- compruebalo
-- Ver los datos de los alquileres de los coches matriculados en la provincia de Las Palmas
select * from alquiler_coches.flota inner join alquiler_coches.distribuidor on flota.ID_dist = distribuidor.ID where ciudad like'Las Palmas%';
-- 4. Realizar una consulta donde me indique las veces que ha sido alquilado cada coche
select distinct Matricula, count(ID_mat) as "Nº Alquileres" from alquiler inner join flota on ID_mat = Flota.ID group by ID_mat;
-- 5. Realizar una consulta donde me indique lo que he facturado con cada coche
select Matricula, (fecha_in-fecha_out)*precio_dia as 'Facturación (€)' from flota inner join alquiler on Flota.ID = id_mat group by Matricula;
-- 6. Ver una lista de los alquileres que han excedido de 4 días junto con su precio final
select alquiler.ID, Matricula, fecha_out,fecha_in,fecha_in-fecha_out as Dias,precio_dia, (fecha_in-fecha_out)*precio_dia as 'Facturación (€)'
from alquiler inner join flota on id_mat = Flota.ID where (fecha_in-fecha_out)>4;
-- 7. Ver una lista donde me indique lo que he facturado en cada mes
select month(fecha_in) as mes, (fecha_in-fecha_out)*precio_dia as 'Reacudación (€)' from alquiler inner join flota on id_mat = Flota.ID group by month(fecha_in);
-- 8. Realizar una consulta donde vea que la fecha de salida haya sido en fin de semana (sábado o domingo)
select *,dayofweek(fecha_in) as 'Día semana' from alquiler where dayofweek(fecha_in)=1 or dayofweek(fecha_in)=7;
-- 9. Insertar una matricula (por parámetro) y ver los alquileres que se han realizado con ese coche junto con el precio final
select matricula,  fecha_out, fecha_in, usuario, user_phone, observaciones, count(matricula) as NºAlquileres
from alquiler_coches.alquiler inner join alquiler_coches.flota on 
ID_mat=Flota.ID group by matricula;
-- 10. Insertar un distribuidor (por parámetro) y visualizar los alquileres con los coches de ese distribuidor
select nombre_dist,fecha_out,fecha_in,usuario,user_phone,observaciones,count(nombre_dist) as NºAlquileres
from alquiler_coches.alquiler inner join alquiler_coches.Flota on 
ID_mat=Flota.ID inner join distribuidor on ID_dist=distribuidor.ID group by nombre_dist;