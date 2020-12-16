/* 1 Devuelve un listado con todos los empleados junto con los datos de los departamentos donde trabajan. 
Este listado también debe incluir los empleados que no tienen ningún departamento asociado.
*/
/*
select concat(empleado.nombre,' ',apellido1,' ',ifnull(apellido2,'')) as Empleado, departamento.nombre 
from empresa.empleado right join empresa.departamento on ID_departamento=departamento.ID;*/  /* No estoy muy seguro de que esto sea lo 
que tenía que obtener. Evidentemente, el ejercicio está mal redactado, ya que ningún empleado carece de departamento, pero si hay 
departamentos carentes de empleado. Supongo que debería buscar todos los departamentos, sin importar que no tengan empleados. */

/*  2	Devuelve un listado donde sólo aparezcan aquellos empleados que no tienen ningún departamento asociado. */
/*
select concat(empleado.nombre,' ',apellido1,' ',ifnull(apellido2,'')) as Empleado, departamento.nombre 
from empresa.empleado right join empresa.departamento on ID_departamento=departamento.ID where isnull(apellido1); -- Idemly
*/

/* 3.	Devuelve un listado donde sólo aparezcan aquellos departamentos que no tienen ningún empleado asociado. */
/*
select concat(empleado.nombre,' ',apellido1,' ',ifnull(apellido2,'')) as Empleado, departamento.nombre 
from empresa.empleado right join empresa.departamento on ID_departamento=departamento.ID where not isnull(apellido1);
*/

/* 4.	Devuelve un listado con todos los empleados junto con los datos de los departamentos donde trabajan. 
El listado debe incluir los empleados que no tienen ningún departamento asociado y los departamentos que no 
tienen ningún empleado asociado. Ordene el listado alfabéticamente por el nombre del departamento.
*/
/*
select concat(empleado.nombre,' ',apellido1,' ',ifnull(apellido2,'')) as Empleado, departamento.nombre 
from empresa.empleado right join empresa.departamento on
ID_departamento=departamento.ID; -- de nuevo, no hay empleados sin departamento.alter
*/
/*5.	Devuelve un listado con los empleados que no tienen ningún departamento asociado y los departamentos que no tienen
ningún empleado asociado. Ordene el listado alfabéticamente por el nombre del departamento.
*/
-- yo paso...