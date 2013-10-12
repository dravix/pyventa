DELETE FROM codigos where producto in (select ref from productos where familia in (select id from familias where departamento=2))
DELETE FROM productos where familia in (select id from familias where departamento=2)
