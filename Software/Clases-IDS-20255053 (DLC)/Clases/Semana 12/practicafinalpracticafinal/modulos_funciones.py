#Registro de Estudiante

from modulo_datos import estudiantes, cursos

def Registro():
    existe = False
    carnet_R = input("Ingrese Carnet: ")
    if len(carnet_R) >= 6 and len(carnet_R) <=10:
        existe == True
        print("Carnet es valido")
    else:
        print("Carnet NO es valido")
        return
    
    for E in estudiantes:
        if E["carnet"] == carnet_R:
            print("existe")
            return
    
    nombre = input("Ingresa tu nombre: ")
    if len(nombre) < 2:
        print("Nombre NO valido")
        return
        
    apellido = input("Ingresa tu apellido: ")
    if len(apellido) < 2:
        print("Apellido NO valido")
        return
    
    estudiantes.append({"carnet": carnet_R, "nombre": nombre, "Apellid": apellido})
    Cursos.append({"carnet": carnet_R, "curso":""})
    
    return

def Cursos():
    cursos_R = input("Ingrese el carnet")
    if cursos_R.lower() == "salir":
        return
    
    for C in cursos:
        if C["carnet"] != cursos_R:
            return
        if C["curso"] != "":
            return
    print("Hola mundo")