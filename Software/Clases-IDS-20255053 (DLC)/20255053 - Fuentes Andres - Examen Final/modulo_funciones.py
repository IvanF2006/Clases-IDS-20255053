"Por mi honor y ante mis compañeros, me comprometo a no copiar, para que este examen refle mi verdadero nivel de conocimientos."    

#Codigo de honor

import modulo_datos as DATOS
from modulo_datos import diccionario_de_clientes
#Imports de los datos para extraer y enviar

def registrar_cliente():

    Nombre_del_cliente = input("Ingrese su nombre: ")
    #Pide nombre del cliente
    
    Correo_electronico = input("Ingrese su correo electronico: ")
    #Pide correo del cliente
    
    if len(Nombre_del_cliente) > 2:
        print(f"Nombre: {Nombre_del_cliente}")
    else:
        print("Nombre NO valido.")
    #Validacion del nombre del cliente
    
    if Correo_electronico.count(" ") > 0:
        print("Correo NO valido.")
    elif Correo_electronico == "CorreoElectronico":
        print("Correo existente")
    else:
        Correo_electronico.append
        print(f"Correo: {Correo_electronico}")
    #Validacion del corre
    


def registrar_pedido():
    
    Solicitar_correo = input("Ingrese su correo electronico: ")
    
    if Solicitar_correo.lower() == "salir":
        return



"""
import modulo_datos as md

def registrar_cliente():
    nombre = input("Ingrese su nombre: ")
    #pide nombre
    
    if len(nombre) < 3:
        print("Nombre NO valido")
        return
    #verifica que el nombre no sea menor de dos caracteres

    correo = input("Ingrese su correo electronico: ")
    #pide correo
    
    if correo.count(" ") > 0:
        print("Correo NO valido")
        return
    #verifica que el correo no tenga espacios
    
    elif len(correo) <= 0:
        print("Corre NO valido")
        return
    #verifica que el correo no este vacio
"""
#IGNORAR
    
    
    
    
    