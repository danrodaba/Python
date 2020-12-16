-- 1 Lista el primer apellido de todos los empleados.

-- select apellido1 from empresa.empleado;

-- 2 Lista el primer apellido de los empleados eliminando los apellidos que estén repetidos.

-- select distinct apellido1 from empresa.empleado;

-- 3 Lista todas las columnas de la tabla empleado.

-- select * from empresa.empleado;

-- 4 Lista el nombre y los apellidos de todos los empleados.

-- select nombre,apellido1,apellido2 from empresa.empleado;

-- 5 Lista el código de los departamentos de los empleados que aparecen en la tabla empleado.

-- select ID_departamento from empresa.empleado;

-- 6 Lista el código de los departamentos de los empleados que aparecen en la tabla empleado, eliminando los códigos que aparecen repetidos.

-- select distinct ID_departamento from empresa.empleado;

-- 7 Lista el nombre y apellidos de los empleados en una única columna.

-- select concat(nombre, ' ' , apellido1, ' ' ,  ifnull(apellido2,'')) as 'Empleado' from empresa.empleado;

-- 8 Lista el nombre y apellidos de los empleados en una única columna, convirtiendo todos los caracteres en mayúscula.

-- select upper(concat(nombre, ' ',apellido1, ' ',ifnull(apellido2,''))) as 'Empleado' from empresa.empleado;

-- 9 Lista el nombre y apellidos de los empleados en una única columna, convirtiendo todos los caracteres en minúscula.

-- select lower(concat(nombre,' ' ,apellido1, ' ', ifnull(apellido2,''))) as 'Empleado' from empresa.empleado;

/* 10 Lista el código de los empleados junto al nif, pero el nif deberá aparecer en dos columnas, 
una mostrará únicamente los dígitos del nif y la otra la letra.*/

select concat(nombre,' ' ,apellido1, ' ', ifnull(apellido2,'')) as 'Empleado',
substr(NIF,1,8) as "Parte numérica", substr(NIF,9,1) as "Letra" from empresa.empleado;

/* 11 Lista el nombre de cada departamento y el valor del presupuesto actual del que dispone. 
Para calcular este dato tendrá que restar al valor del presupuesto inicial (columna presupuesto)
los gastos que se han generado (columna gastos). Tenga en cuenta que en algunos casos pueden existir 
valores negativos. Utilice un alias apropiado para la nueva columna columna que está calculando.*/

-- select nombre as 'Departamento' , presupuesto - gastos as 'Líquido' from empresa.departamento;

-- 12 Lista el nombre de los departamentos y el valor del presupuesto actual ordenado de forma ascendente.

-- select nombre as 'Departamento', presupuesto - gastos as 'Líquido' from empresa.departamento order by presupuesto - gastos asc;

-- 13 Lista el nombre de todos los departamentos ordenados de forma ascendente.

-- select nombre as 'Departamentos' from empresa.departamento order by nombre;

-- 14 Lista el nombre de todos los departamentos ordenados de forma desscendente.

-- select nombre as 'Departamentos' from empresa.departamento order by nombre desc;

/* 15 Lista los apellidos y el nombre de todos los empleados, ordenados de forma alfabética 
tendiendo en cuenta en primer lugar sus apellidos y luego su nombre. */

-- select concat(apellido1, ' ', ifnull(apellido2,''), ' ', nombre) as empleado from empresa.empleado order by apellido1, apellido2, nombre;

-- 16 Devuelve una lista con el nombre y el presupuesto, de los 3 departamentos que tienen mayor presupuesto.

-- select nombre as 'Departamento', presupuesto as 'Presupuesto' from empresa.departamento order by presupuesto desc limit 3;

-- 17 Devuelve una lista con el nombre y el presupuesto, de los 3 departamentos que tienen menor presupuesto.

-- select nombre as 'Departamento', presupuesto as 'Presupuesto' from empresa.departamento order by presupuesto asc limit 3;

-- 18 Devuelve una lista con el nombre y el gasto, de los 2 departamentos que tienen mayor gasto. ¿Estás de coña?

-- select nombre as 'Departamento', gastos as 'Gastos' from empresa.departamento order by gastos desc limit 2;

-- 19 Devuelve una lista con el nombre y el gasto, de los 2 departamentos que tienen menor gasto. 

-- select nombre as 'Departamento', gastos as 'Gastos' from empresa.departamento order by gastos asc limit 2; -- MempiesoaponerbiolemtoDiosmeo!

/* 20 Devuelve una lista con 5 filas a partir de la tercera fila de la tabla empleado. La tercera fila se 
debe incluir en la respuesta. La respuesta debe incluir todas las columnas de la tabla empleado.*/

-- select ID, concat(nombre, ' ', apellido1, ' ', ifnull(apellido2,'')) as 'Empleado' from empresa.empleado where ID between 3 and 7;

/* 21 Devuelve una lista con el nombre de los departamentos y el presupuesto, de aquellos que tienen un presupuesto mayor o 
igual a 150000 euros. */

-- select nombre as 'Departamento', presupuesto as 'Presupuesto' from empresa.departamento where presupuesto >= 150000;

/* 22 Devuelve una lista con el nombre de los departamentos y el gasto, de aquellos que tienen menos de 5000 euros de gastos. */

-- select nombre as 'Departamento', presupuesto as 'Presupuesto' from empresa.departamento where presupuesto <= 5000;

/* 23 Devuelve una lista con el nombre de los departamentos y el presupesto, de aquellos que tienen un presupuesto 
entre 100000 y 200000 euros. Sin utilizar el operador BETWEEN. */

-- select nombre as 'Departamento', presupuesto as 'Presupuesto' from empresa.departamento where presupuesto <= 200000 and presupuesto>= 100000;

/* Devuelve una lista con el nombre de los departamentos que no tienen un presupuesto entre 100000 y 200000 euros. 
Sin utilizar el operador BETWEEN.*/

-- select nombre as 'Departamento', presupuesto as 'Presupuesto' from empresa.departamento where presupuesto >= 200000 or presupuesto<= 100000;

/* Devuelve una lista con el nombre de los departamentos que tienen un presupuesto entre 100000 y 200000 euros. 
Utilizando el operador BETWEEN.*/

-- select nombre as 'Departamento', presupuesto as 'Presupuesto' from empresa.departamento where presupuesto between 100000 and 200000; -- menfado

/* Devuelve una lista con el nombre de los departamentos que no tienen un presupuesto entre 100000 y 200000 euros. 
Utilizando el operador BETWEEN.*/

-- select nombre as 'Departamento', presupuesto as 'Presupuesto' from empresa.departamento where presupuesto not between 100000 and 200000; -- mucho

/* 27 Devuelve una lista con el nombre de los departamentos, gastos y presupuesto, de aquellos departamentos donde los gastos 
sean mayores que el presupuesto del que disponen. */

-- select nombre as 'Departamento', gastos as 'Gastos', presupuesto as 'Presupuesto' from empresa.departamento where gastos > presupuesto;

/* 27 Devuelve una lista con el nombre de los departamentos, gastos y presupuesto, de aquellos departamentos donde los gastos sean menores 
que el presupuesto del que disponen. */

-- select nombre as 'Departamento', gastos as 'Gastos', presupuesto as 'Presupuesto' from empresa.departamento where gastos < presupuesto;

/* 29 Devuelve una lista con el nombre de los departamentos, gastos y presupuesto, de aquellos departamentos donde los gastos sean iguales al 
presupuesto del que disponen. */

-- select nombre as 'Departamento', gastos as 'Gastos', presupuesto as 'Presupuesto' from empresa.departamento where gastos = presupuesto; -- copio por aquí, pego por allá...

-- 30 Lista todos los datos de los empleados cuyo segundo apellido sea NULL.

-- select * from empresa.empleado where isnull(apellido2);

-- 31 Lista todos los datos de los empleados cuyo segundo apellido no sea NULL.

-- select * from empresa.empleado where not isnull(apellido2);

-- 32 Lista todos los datos de los empleados cuyo segundo apellido sea López.

-- select * from empresa.empleado where apellido2 = 'López';

-- 33 Lista todos los datos de los empleados cuyo segundo apellido sea Díaz o Moreno. Sin utilizar el operador IN.

-- select * from empresa.empleado where apellido2 = 'Díaz' or apellido2 = 'Moreno' or apellido2='Diaz';

-- 34 Lista todos los datos de los empleados cuyo segundo apellido sea Díaz o Moreno. Utilizando el operador IN.

-- select * from empresa.empleado where apellido2 in('Díaz','Moreno','Diaz');

-- 35 Lista los nombres, apellidos y nif de los empleados que trabajan en el departamento 3.

-- select NIF, concat(nombre,' ',apellido1,' ',ifnull(apellido2,'')), ID_departamento as 'Empleado'  from empresa.empleado where ID_departamento = 3;

-- 36 Lista los nombres, apellidos y nif de los empleados que trabajan en los departamentos 2, 4 o 5.

-- select NIF, concat(nombre,' ',apellido1,' ',ifnull(apellido2,'')), ID_departamento as 'Empleado'  from empresa.empleado where ID_departamento in (2,4,5);