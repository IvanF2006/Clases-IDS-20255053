import modulos_funciones
import modulo_datos
from modulo_datos import estudiantes

Menu = True

while Menu == True:
    print("""Menu
1.Registro de estudiantes
2.Inscribir Curso
3.Generar Reportes
4.salir
      """)
    seleccion = input("Ingrese una opcion del [1-4]: ")
    if seleccion == "1":
        print(modulo_datos.estudiantes)
        modulos_funciones.Registro()
        
    if seleccion == "5":
        print(modulo_datos.estudiantes)
        
    elif seleccion == "2":
        modulos_funciones.Cursos()
    
    elif seleccion == "3":
        print("3 xd")
        
    elif seleccion == "4":
        print("Los amo padres")
        break
    