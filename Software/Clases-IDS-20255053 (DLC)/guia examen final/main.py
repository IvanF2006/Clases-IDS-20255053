#inicio del sistema

import modulo_funciones as mf

while True:
    print("Bienvenido al sistema. Seleccione una opción: (1-4)")
    print("1. Registrar estudiante")
    print("2. Inscrbir curso")
    print("3. Generar reportes")
    print("4. Salir")
    opcion = input("Elija una opción: ")
    if opcion == "1":
        mf.registrar_estudiante()
    elif opcion == "2":
        mf.inscribir_curso()
    elif opcion == "3":
        mf.generar_reportes()
    elif opcion == "4":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida. Por favor, intente otra.")           