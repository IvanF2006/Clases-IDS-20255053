#Construir funciones

import modulo_datos as md

def registrar_estudiante():
    '''Función para registrar y validar un estudiante'''
    while True:    
        carnet_1 = input("Ingrese el carnet del estudiante: ")
        largo_carnet = len(carnet_1)
        
        existe = False
        for estu in md.estudiantes:
            if estu["carnet"] == carnet_1:
                existe = True
                print("El carnet ya existe. Intente de nuevo.")
                break
            if existe:
                continue
            
        if largo_carnet >= 6 and largo_carnet <= 10 and existe == False:
            print("Carnet válido.")
            break
        else:
            print("Carnet inválido.")
            
    while True:    
        nombre_1 = input("Ingrese el nombre del estudiante: ")
        if len(nombre_1)>1:
            break
        else:
            print("El nombre no tiene el largo requerido")
    while True:
        apellido_1 = input("Ingrese el apellido del estudiante: ")
        if len(apellido_1)>1:
            break
        else:
            print("El apellido no tiene el largo requerido")
        
    md.estudiantes.append({
        "carnet": carnet_1,
        "nombre": nombre_1,
        "apellido": apellido_1
    })
    print(md.estudiantes)

def inscribir_curso():
    '''Función para inscribir un curso a un estudiante
    A IVAN LE GUSTAN LAS YEGUAS DE UMAMUSUME'''
    while True:
        carnet_2 = input("Ingrese el carnet del estudiante a inscribir: ")
        existe = False
        for estu in md.estudiantes:
            if estu["carnet"] == carnet_2:
                existe = True
                
        if existe:
            print("Estudiante encontrado.")
            print("Cursos disponibles:")
            
            while True:
                
                for codigo, nombre in md.cursos.items(): 
                    print(f"{codigo}: {nombre}")
                
                curso_1 = input("Ingrese el código del curso a inscribir (o 'salir'): ")
                
                if curso_1.lower() == 'salir':
                    print("Saliendo de inscripción de curso.")
                    break
                
                repetido = False
                for carnet_i, curso_i in md.inscripciones:
                    if carnet_i == carnet_2 and curso_i == curso_1:
                        repetido = True
                        break

                if repetido:
                    print("El estudiante YA tiene inscrito este curso.")
                    break

                if curso_1 not in md.cursos:
                    print("Código de curso inválido. Intente de nuevo.")
                    break
            
                md.inscripciones.append((carnet_2, curso_1))
                print("Inscripción realizada con éxito.")
                print(md.inscripciones)
                break
            break
        else:
            print("Estudiante no encontrado. Intente con otro carnet.")
            
def generar_reportes():
    '''Genera reportes según las inscripciones registradas'''

    if len(md.inscripciones) == 0:
        print("No hay inscripciones registradas.")
        return

    while True:
        print("MENU DE REPORTES")
        print("1. PY - Python Básico")
        print("2. JS - JavaScript para Principiantes")
        print("3. BD - Introducción a Bases de Datos")
        print("4. SE - Seguridad en Entornos Digitales")
        print("5. Estudiantes sin inscripción")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "6":
            print("Regresando")
            break

        if opcion == "1":
            curso = "PY"
        elif opcion == "2":
            curso = "JS"
        elif opcion == "3":
            curso = "BD"
        elif opcion == "4":
            curso = "SE"
        elif opcion == "5":
            curso = "SIN"
        else:
            print("Opción inválida.")
            continue

        if curso == "SIN":
            print("Estudiantes sin inscripción:")

            carnets_inscritos = []
            for carnet_i, curso_i in md.inscripciones:
                carnets_inscritos.append(carnet_i)

            encontrados = False
            for estu in md.estudiantes:
                if estu["carnet"] not in carnets_inscritos:
                    print(f"{estu['carnet']} - {estu['nombre']}")
                    encontrados = True

            if not encontrados:
                print("Todos los estudiantes tienen al menos una inscripción.")

            continue

        print(f"Estudiantes en {curso}")

        encontrados = False
        for carnet_i, curso_i in md.inscripciones:
            if curso_i == curso:
                print(carnet_i)
                encontrados = True

        if not encontrados:
            print("No hay estudiantes inscritos en este curso.")