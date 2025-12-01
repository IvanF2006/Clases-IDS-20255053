#Modulo administrativo

#Importacion de los modulos que se van a usar
import modulo_datos
import modulo_funciones as fn #as es para ponerle alias a las weas y hacerlo mas corto y simple y aha

menu = True #Variable que indica que el menu se esta ejecutando

while menu:
    print("""    ----------Menu Principal---------
    1. Registrar estudiante       
    2. Inscribir en curso         
    3. Generar reportes           
    4. Salir    
    ---------------------------------                  
""")
    opcion = input("Elija la opcion: ")
    if opcion == "1":
        fn.registrar_estudiante()
    elif opcion == "2":
        print("Eligio 2")
    elif opcion == "3":
        print("Eligio 3")
    elif opcion == "4":
        menu = False
        print("Gracias por elegir nuestro servicio")
    else:
        print("Opcion no valida")