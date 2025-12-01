#Definiciones de nuestro sistema

#Importamos la estructura de datos
import modulo_datos as dat

def registrar_estudiante():
    """Vamos a registrar un estudiante (carnet, nombre y apellido)"""
    while True:
        carnet_i = input("Ingrese numero de carnet: ") #La funcionalidad de los carnets NO son numericas asi que no es necesario convertirlos a enteros ya que aha no sacas promedio de carnets y ondas asi por eso Alvin no convierte la onda y aha
        existe = False
        for c in dat.estudiantes:
            if c["carnet"] == carnet_i:
                existe = True
        if len(carnet_i) >= 6 and len(carnet_i) <= 10 and existe == False:
            break
        print("El carnet debe ser entre 6 y 10 caracteres, y ser unico.")
    while True:
        nombre_i = input("Ingrese el nombre: ")
        if len(nombre_i) > 2:
            break
        print("El nombre no debe ser menor a dos caracteres")
    while True:
        apellido_i = input("Ingrese el apellido: ")
        if len(apellido_i) > 2:
            break
        print("El apellido no debe ser menor a dos caracteres")
    dat.estudiantes.append(
        {
            "carnet" : carnet_i,
            "nombre" : nombre_i,
            "apellido" : apellido_i
        }
    )
#Alvin asi too sensei explica como es mejor ir en poquito a poquito en vez de preocuparse por andar viendo si el carnet es solo numero y cuestiones asi