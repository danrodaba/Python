-- 1 Devuelve un listado con los empleados y los datos de los departamentos donde trabaja cada uno.
/*
select concat(empleado.nombre,' ',apellido1,' ',ifnull(apellido2,'')) as 'Empleado', 
departamento.nombre as 'Departamento' from empresa.empleado inner join empresa.departamento 
on empresa.empleado.ID_departamento = empresa.departamento.ID;
*/

/* 2 Devuelve un listado con los empleados y los datos de los departamentos donde trabaja cada uno. 
Ordena el resultado, en primer lugar por el nombre del departamento (en orden alfabético) y 
en segundo lugar por los apellidos y el nombre de los empleados.
*/
/*
select concat(empleado.nombre,' ',apellido1,' ',ifnull(apellido2,'')) as 'Empleado',
departamento.nombre as 'Departamento' from empresa.empleado inner join empresa.departamento on
ID_departamento = departamento.ID order by departamento.nombre desc, apellido1, apellido2, empleado.nombre;
*/
-- 3 Devuelve un listado con el código y el nombre del departamento, solamente de aquellos departamentos que tienen empleados.
/*
select distinct departamento.ID, departamento.nombre 
from empresa.departamento inner join empresa.empleado on
departamento.ID=ID_departamento;
*/

/* 4 Devuelve un listado con el código, el nombre del departamento y el valor del presupuesto actual del que dispone, 
solamente de aquellos departamentos que tienen empleados. El valor del presupuesto actual lo puede calcular restando 
al valor del presupuesto inicial (columna presupuesto) el valor de los gastos que ha generado (columna gastos).
*/
/*
select distinct departamento.ID, departamento.nombre, presupuesto-gastos
from empresa.departamento inner join empresa.empleado on
departamento.ID=ID_departamento;
*/
-- 5 Devuelve el nombre del departamento donde trabaja el empleado que tiene el nif 38382980M.
/*
select departamento.nombre
from empresa.departamento inner join empresa.empleado on 
departamento.ID=ID_departamento where NIF='38382980M';
*/
-- 6 Devuelve el nombre del departamento donde trabaja el empleado Pepe Ruiz Santana.
/*
select departamento.nombre
from empresa.departamento inner join empresa.empleado on
 departamento.ID=ID_departamento where empleado.nombre='Pepe' and apellido1='Ruiz' and apellido2='Santana';
 */
 
-- 7 Devuelve un listado con los datos de los empleados que trabajan en el departamento de I+D. Ordena el resultado alfabéticamente.
/*
select concat(empleado.nombre,' ',apellido1,' ',ifnull(apellido2,'')) as Empleado, departamento.nombre from empresa.departamento inner join empresa.empleado on
departamento.ID = ID_departamento where departamento.nombre = 'I+D';
*/

/* 8 Devuelve un listado con los datos de los empleados que trabajan en el departamento de Sistemas, 
Contabilidad o I+D. Ordena el resultado alfabéticamente.
*/
/*
select concat(empleado.nombre,' ',apellido1,' ',ifnull(apellido2,'')) as Empleado, departamento.nombre
from empresa.departamento inner join empresa.empleado on departamento.ID= ID_departamento
where departamento.nombre in ('Sistemas','Contabilidad','I+D');
*/
/* 9 Devuelve una lista con el nombre de los empleados que tienen los departamentos 
que no tienen un presupuesto entre 100000 y 200000 euros.
*/
/*
select concat(empleado.nombre,' ',apellido1,' ',ifnull(apellido2,'')) as Empleado, departamento.nombre, presupuesto-gastos 
from empresa.empleado inner join empresa.departamento on
ID_departamento = departamento.ID where presupuesto-gastos not between 100000 and 200000;
*/

/* 10 Devuelve un listado con el nombre de los departamentos donde existe algún empleado cuyo segundo apellido sea NULL. 
Tenga en cuenta que no debe mostrar nombres de departamentos que estén repetidos.
*/

select departamento.nombre, concat(empleado.nombre,' ',apellido1,' ',ifnull(apellido2,'')) as Empleado 
from empresa.empleado inner join empresa.departamento on
ID_departamento = departamento.ID where isnull(apellido2);