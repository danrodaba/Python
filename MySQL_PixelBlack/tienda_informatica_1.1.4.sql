-- ejercicios 1-3

select producto.nombre as "Nombre producto" ,producto.codigo as "Código producto" ,
fabricante.nombre as "Nombre fabricante" ,fabricante.codigo as "Código fabricante"
from tienda.producto inner join tienda.fabricante on 
tienda.producto.codigo_fabricante=tienda.fabricante.codigo order by fabricante.nombre;

-- ejercicios 4 - 5

select producto.nombre as "Nombre producto" ,producto.precio as "Precio (€)" , fabricante.nombre as "Nombre fabricante" 
from tienda.producto inner join tienda.fabricante on 
tienda.producto.codigo_fabricante=tienda.fabricante.codigo order by precio desc limit 1;

-- ejercicio 6 - 7
select producto.nombre as "Nombre producto" ,producto.precio as "Precio (€)" , fabricante.nombre as "Nombre fabricante" 
from tienda.producto inner join tienda.fabricante on 
tienda.producto.codigo_fabricante=tienda.fabricante.codigo where fabricante.nombre="Crucial" and precio > 200;

-- ejercicio 8
select producto.nombre as "Nombre producto" ,producto.precio as "Precio (€)" , fabricante.nombre as "Nombre fabricante" 
from tienda.producto inner join tienda.fabricante on 
tienda.producto.codigo_fabricante=tienda.fabricante.codigo where fabricante.nombre = "Asus" or fabricante.nombre = "Hewlett-Packard" or fabricante.nombre = "Seagate";

-- ejercicio 9
select producto.nombre as "Nombre producto" ,producto.precio as "Precio (€)" , fabricante.nombre as "Nombre fabricante" 
from tienda.producto inner join tienda.fabricante on 
tienda.producto.codigo_fabricante=tienda.fabricante.codigo where fabricante.nombre in ("Asus","Hewlett-Packard","Seagate");

-- ejercicio 10 - 12
select producto.nombre as "Nombre producto" ,producto.precio as "Precio (€)" , fabricante.nombre as "Nombre fabricante" 
from tienda.producto inner join tienda.fabricante on 
tienda.producto.codigo_fabricante=tienda.fabricante.codigo where fabricante.nombre like '%e';


-- ejercicio 12
select producto.nombre as "Nombre producto" ,producto.precio as "Precio (€)" , fabricante.nombre as "Nombre fabricante" 
from tienda.producto inner join tienda.fabricante on 
tienda.producto.codigo_fabricante=tienda.fabricante.codigo where precio >180 order by precio desc, producto.nombre asc;

