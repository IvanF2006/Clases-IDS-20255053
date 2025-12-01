#Descripcion
"""
Hay un estreno en el cine, la cola para entrar es larga, el dueño quiere saber cuantos van entrar porque
la pelicula es clasificación B15 que no es recomendada para menores de 15 años. Apoya al dueño creando un programa 
que determine la cantidad que ingresaron a ver la pelicula. 
"""
#Entrada
"""
Una variable entera A que representa la cantidad de personas que hay en la fila y las edades de cada una de las 
personas de la fila. 
"""
#Salida
"""
Un valor entero que representa la cantidad de personas que ingresaron a la sala a ver la pelicula. 
"""

A = int(input()) #Personas que se encuentran en la fila y se repetira el bucle para almacenar sus edades
edadesdetodos=[] #Lista que almacena las edades de todos
numeroenlista = 0 #Que numero de persona ya sea primera o segunda va revisarse si comple la edad
personasquepuedeningresar = [] #Personas mayores o de 15 años
for i in range(A): 
    X = int(input())
    edadesdetodos.append(X)
for i in edadesdetodos:
    if edadesdetodos[numeroenlista] >= 15:
            personasquepuedeningresar.append(edadesdetodos[numeroenlista])
            numeroenlista+=1
            continue
    else:
         numeroenlista+=1
         continue
print(len(personasquepuedeningresar))