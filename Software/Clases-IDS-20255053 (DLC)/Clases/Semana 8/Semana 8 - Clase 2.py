#Vamos a jugar un juego
aprobacion = True

while aprobacion:
    eleccion = input("Quieres seguir jugando?) (Y/N)")
    if eleccion[0].lower() == "n": #La cuestion del [0] es para contar la primera letra ya que quiza un wn quiere poner yes y aha
        aprobacion = False         #asi solo cacha la "y" y no lo demas
    elif eleccion[0].lower() == "y": #una side note es que al usar .lower() el comparador tambien tiene que estar en minuscula
        print("Me alegra que quieras seguir jugando!")
    else:
        print("La opcion elegida no es valida.")

#Bucle definido manualmente
"""      
alumnos = []
        
alumno = input("Digite el nombre: ")
alumnos.append(alumno)
alumno = input("Digite el nombre: ")
alumnos.append(alumno)
alumno = input("Digite el nombre: ")
alumnos.append(alumno)
print(alumnos)
"""

#Bucle definido por inpute
"""
alumnos = []

for a in range(input("Digite la cantidad de alumnos a registrar: ")):
    alumno = input("Digite el nombre: ")
    alumnos.append(alumno)
    
print(alumnos)
"""

#Sistema de gestion de alumnos

menu_iniciado = True
alumnos = []

while menu_iniciado:
    opcion = int(input("1.Agregar, 2.Consultar, 3.Modificar, 4.Borrar, 5.Salir"))
    if opcion == 5:
        menu_iniciado = False
    elif opcion == 1:
        alumnos.append(input("Digite el nombre del alumno: "))
        print(alumnos)
    elif opcion == 2:
        for a in alumnos:
            print(a)
    elif opcion == 3:
        indice = int(input("Digite el numero del alumno (1-3)"))
        nuevo = input("Digite el nombre buevo: ")
        alumnos[indice - 1] = nuevo
    elif opcion == 4:
        indicie = int(input("Digite el numero del alumno (1-3) a pope"))
        alumno_borrado = alumnos.pop(indice - 1)
        print(f"Hemnos borrado a: {alumno_borrado}")
    else:
        print("Esa opcion no es valida")
        
print("Gracias por usar nuestro sistema.")