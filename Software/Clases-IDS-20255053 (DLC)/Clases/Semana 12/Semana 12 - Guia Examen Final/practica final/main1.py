#Indice de sistema

#Importaciones de los modulos necesaarios
import modulo_funciones1 as fn #NO me gusta usar fn pero asi es como al ticher le gusta asi que aha fn es ahora como el nickname de modulo_funciones1

while True:
    print("""  --Menu Principal--
1. Registrar estudiante
2. Inscribir curso
3. Generar reportes
4. Salir
          """)
    
    opcion = input("Elija una opcion [1-4]: ")
    
    if opcion == "1":
        fn.registrar_estudiante() #fn -> y luego la funcion
    elif opcion == "2":
        print("2")
    elif opcion == "3":
        print("3")
    elif opcion == "4":
        print("4")
        break #Se sale del bucle
    else:
        print("Error")