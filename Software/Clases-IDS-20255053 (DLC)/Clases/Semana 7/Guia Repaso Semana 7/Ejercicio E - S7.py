#Descripcion
"""
David hace poco descubrió un videojuego bastante interesante, lo instaló y empezó a practicarlo mucho, tanto que se hizo un 
profesional, sin embargo, a pesar de que sabe que sus combos siempre hacen daño, quiere saber cuánto hacen exactamente. 
Cada combo consta de presionar 6 veces los botones de ataque A, B y/o C. Cada boton hace un daño diferente. 
"""
#Entrada
"""
Un entero N con la cantidad de combos que ejecuto David, Seguido de enteros Pa, Pb, Pc que son la cantidad de daño de los
ataques A,B y C. Despues N lineas con los combos de David 
"""
#Salida
"""
El daño de cada combo de David 
"""

# 1. Declarar un entero N.
# 2. Declarar entero P y dividirlo en Pa Pb y Pc. (Usa listas y map)
# 3. Crear una lista en donde se vayan guardando las variables que se creen en el bucle.
# 4. Hacer un bucle por cada entero desde 0 hasta N para definir el combo
# 5. Crear una variable X=0 que vaya contando cuantas veces se utiliza que letra de los combos
# 6. Crear un bucle con una variable A que cuente las veces de A,B,C separadas
# y que su daño lo almacene en x.
# 7. crear una variable y = 0 que vaya sumando el daño hecho de los combos
# 8. Crear finalmente un bucle que muestre el daño total de cada uno de los combos
N = int(input())
P = list(map(int, input().split(" ")))
Pa = int(P[0])
Pb = int(P[1])
Pc = int(P[2])
combos = []
for elemento in range(N):
    A = input().upper()
    combos.append(A)
daño = []
x = 0
for i in combos:
    A = (combos[x].count("A")*Pa)+(combos[x].count("B")*Pb)+(combos[x].count("C")*Pc)
    daño.append(A)
    x +=1 #Se me habia olvidado poner esto XD
y = 0
for i in daño:
    print(daño[y])
    y+=1