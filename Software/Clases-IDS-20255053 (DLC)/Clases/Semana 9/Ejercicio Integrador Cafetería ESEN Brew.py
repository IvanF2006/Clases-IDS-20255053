"""
Ejercicio Integrador: Cafetería ESEN Brew 
Objetivo:
Aplicar el uso combinado de listas, diccionarios, bucles y estructuras de control para simular un sistema básico 
de gestión de una cafetería, introduciendo el concepto de códigos únicos (como claves en una base de datos). 
•	Claves únicas (como identificadores primarios).
•	Relaciones entre entidades (cliente–pedido, producto–pedido).
•	Validaciones basadas en esas relaciones.
Instrucciones:
La cafetería ESEN Brew necesita un sistema que le permita:
Registrar clientes (con un código único, nombre, correo y teléfono).
Administrar un menú de productos (con código, nombre, categoría y precio).
Registrar pedidos, donde cada pedido pertenece a un cliente y contiene varios productos.
Deberás crear un programa que muestre un menú de opciones en consola y permita realizar estas acciones.
Estructura del programa:
•	Clientes
•	Cada cliente tiene un código único (por ejemplo: C001, C002), un nombre, correo y teléfono.
•	Se almacenan en una lista de diccionarios.
•	Productos
•	Cada producto tiene un código único (por ejemplo: P001, P002), un nombre, categoría y precio.
•	También se almacenan en una lista de diccionarios.
•	Pedidos
•	Cada pedido se asocia con el código del cliente y una lista de códigos de productos.
•	Incluye además el total calculado automáticamente.
Menú principal:
1.	Mostrar productos
2.	Agregar producto
3.	Registrar nuevo cliente
4.	Mostrar clientes
5.	Registrar pedido
6.	Mostrar pedidos del día
7.	Mostrar categorías disponibles
8.	Salir
"""

productos = []
clientes = []
codigos = []
categorias = [] 
precios = []

p_v_p_mancoijueputas_tengo_la_sala_activa_boom = True

while p_v_p_mancoijueputas_tengo_la_sala_activa_boom == True:
    opciones = int(input("""1.Mostrar productos
2.Agregar producto
3.Registrar nuevo cliente
4.Mostrar clientes
5.Registrar pedido
6.Mostrar pedidos del dia
7.Mostrar categorias disponibles
8.Salir
"""))

    if opciones == 1:
        print()
    elif opciones == 2:
        print()
    elif opciones == 3:
        print()
    elif opciones == 4:
        print()
    elif opciones == 5:
        print()
    elif opciones == 6:
        print()
    elif opciones == 7:
        print()
    elif opciones == 8:
        print()
    else:
        print("Opcion no valida... \n")