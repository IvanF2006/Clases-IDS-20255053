#Descripcion
"""
Leer un numero entero S y mostrar como salida el numero par posterior y el número impar anterior. 
"""
#Entrada
"""
Un número entero S. 
"""
#Salida
"""
El número par posterior y el número impar anterior al número entero leído. 
"""
NumeroS = int(input())

if NumeroS % 2 == 0: #el % lo que hace es dividirlo entre 2 y busca si tiene residuo ya que si lo tiene no es par
    print(NumeroS+2)
    print(NumeroS-1)
else: #lo que se ejecuta cuandono es impar
    print(NumeroS+1)
    print(NumeroS-2)