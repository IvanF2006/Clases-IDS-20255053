#Descripcio
"""
En el siguiente problema recibirá una lista de números y tu tarea será contar cuantos números son 7 y cuantos números son 5 
"""
#Entrada
"""
Un numero entero N que indica cuantos números serán ingresados, seguido de la lista de N números 
"""
#Salida
"""
Dos números enteros indicando cuantos números son 7 y cuantos números son 5, 
el primer número indica cuantos 7 hay y el segundo número indica cuantos 5 hay 
"""

Cantida = int(input())
Numeros = []

for c in range(Cantida):
    numero = int(input())
    Numeros.append(numero)
print(Numeros.count(7),Numeros.count(5))