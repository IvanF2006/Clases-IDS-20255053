"Por mi honor y ante mis compañeros, me comprometo a no copiar, para que este examen refle mi verdadero nivel de conocimientos."    

#Codigo de honor (toda documentacion estara abajo del codigo que este aha documentando y tal)


"""
-Clientes registerados
-Sabores ofrecidos
-Pedidos realizados
"""

import modulo_funciones
import modulo_datos
from modulo_datos import diccionario_de_clientes
#Imports de los otros archivos que se usaran en main.py

Activacion = True
#Activasion del menu para que aparezca


while Activacion == True:
#Bucle while para que siga apareciendo el menu y tal
    
    print("""
    Menu de Cony Cookie:
    1.Registrar cliente
    2.Registrar pedido
    3.Ver reportes
    4.Salir
""")
    
    Seleccion = input("Seleccione una opcion [1-4]: ")

    if Seleccion == "1":
        modulo_funciones.registrar_cliente()
    #Opcion 1
        
    elif Seleccion == "2":
        modulo_funciones.registrar_pedido()
    #Opcion 2
    
    elif Seleccion == "3":
        print("3")
        break
    #Opcion 3
    
    elif Seleccion == "4":
        print("Saliendo...")
        break
    #Opcion 4
    
    elif Seleccion.lower() == "salir":
        print("Saliendo...")
        break
    #aunque con las indicaciones no me queda claro si esto esta correcto o tengo que crear otra opcion de salir ya que en el paper se menciona dos veces que el archivo tiene que tener la funcionalidad de salir
    
    elif Seleccion == "67":
        print(diccionario_de_clientes)
    
    else:
        print("Opcion NO valida")



"""
import modulo_funciones as mf

Encendido = True
#para ver si se tiene que mostrar el menu si o no

while Encendido == True:
#Simpre y cuando sea true se va mantener en bucle haciendo que salga el menu    
    
    print
Menu de Cony Cookie
1.Registrar cliente
2.Registrar pedido
3.Ver reportes
4.Salir
          
    )
#menu que se va mostrar

    Opciones = input("Seleccione una opcion [1-4]: ")
    #lo que el usuario va tener que escribir para acceder a cada opcion
    
    if Opciones == "1":
        mf.registrar_cliente()
    #opcion 1
    
    elif Opciones == "4":
        print("Cerrando programa...")
        Encendido = False
        break
    #opcion 4
    
    elif Opciones.lower() == "salir":
        print("Cerrando programa...")
        Encendido = False
        break
    #al escribir salir se sale
    
    else:
        print
Opcion NO valida.
              )
    #en caso de elegir una opcion no valida
"""
#IGNORAR