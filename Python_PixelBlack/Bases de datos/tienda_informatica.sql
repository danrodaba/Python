select nombre from tienda.producto;
select nombre,precio from tienda.producto;
select * from tienda.producto;
select nombre,precio*1.13,precio from tienda.producto;
select nombre as "Nombre producto" ,precio as "Precio (€)"  from tienda.producto;
select upper(nombre) as "Nombre producto" ,precio as "Precio (€)"  from tienda.producto;
select lower(nombre) as "Nombre producto" ,precio as "Precio (€)"  from tienda.producto;
select producto.nombre as "Nombre producto" ,precio as "Precio (€)", upper(fabricante.nombre) from tienda.producto inner join tienda.fabricante on tienda.producto.codigo_fabricante=tienda.fabricante.codigo;
select nombre as "Nombre producto" ,round(precio) as "Precio (€)"  from tienda.producto;
select nombre as "Nombre producto" ,(precio) as "Precio (€)"  from tienda.producto;
