"""
def calcular_impuesto():
    pass 
"""
#pass es como continue sin importar que

"""
monto = input("Monto a calcular: ")

impuesto = monto + 25
""" 
#Este es error forzado ya que estas intentando sumar texto con numero y seria un error de tipo (TypeError)

while True: #Se va a ejecutar hasta que se calcule bien
    try:
        monto = int(input("Monto a calcular: "))
    except TypeError as te:
        print("Se genera un error: ", te)
    except ValueError as ve:
        print("Es un error de valor.", ve)
    except:
        print("Ese tipo de valores no es valido.")
    else: #Si no hay una excepecion (except) haz el else
        impuesto = monto + 25
        print(f"El valor del impuesto es de ${impuesto:,.2f}")
        break #El break aqui hace que se salga del while pero que se siga ejecutando lo que quede
    finally: #Independientemente de todo muestre esto
        print("Hemos terminado la ejecucion de esta pregunta.")
        
#Framework = coleccion de librerias