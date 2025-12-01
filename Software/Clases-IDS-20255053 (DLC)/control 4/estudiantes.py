'''2. Estudiantes
Guardados en una lista de diccionarios.
Cada estudiante tiene:
•	carnet (ej. S001, S002) — único
•	nombre
2.	Registrar estudiante (15 puntos)
Crear una función:
def registrar_estudiante(lista_estudiantes):
Debe:
•	Pedir el nombre
•	Generar el carnet automáticamente (S001, S002, …)
•	Guardarlo en la lista
'''

def registrar_estudiante(lista_estudiantes):
    nombre = input('Ingrese el nombre del estudiante: ').capitalize()
    
    codigocarnet = len(lista_estudiantes) + 1 #lo mismo que lee cuantos hay le suma uno para que asi luego termine como en el ejemplo
    carnet = f'S{codigocarnet:03d}'
    
    estudiante = { #Y bueno mas de lo mismo aqui el diccionario del estudiante
        "Nombre: ": nombre,
        "Carnet: ": carnet
    }
    
    lista_estudiantes.append(estudiante)#Añade a la lista el estudiante
    
def mostrar_estudiantes(lista_estudiantes):#Lo mismo de que si no hay estudiantes no hay :vv
    if lista_estudiantes == []:
        print("No hay estudiantes")
    else:
        for estudiantes in lista_estudiantes:
            print(estudiantes["Carnet: "], estudiantes["Nombre: "]) #Y bueno lo saca del diccionario y los printea