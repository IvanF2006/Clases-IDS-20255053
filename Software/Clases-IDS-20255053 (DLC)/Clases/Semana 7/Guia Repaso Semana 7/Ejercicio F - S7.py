#Descripcio
"""
Bodoque es un conejo que ha sufrido muchos desamores por distintas razones (aunque no quiso decir por qué).
Ahora, ha vuelto a enamorarse, pero su amigo "D"le ha advertido que no se ilusione demasiado rápido. 
Según él, Bodoque siempre se emociona demasiado y acaba saliendo lastimado.

Por eso, D quiere tu ayuda para saber si esta vez el amor de Bodoque tiene posibilidades de funcionar. 
Ha descubierto que Bodoque toma en cuenta la cantidad de letras en los nombres de sus enamoramientos 
para decidir si debe ilusionarse o no. Si el nombre cumple con ciertas condiciones, él se deja llevar por la emoción.

¡Ayuda a D a evitar que Bodoque sufra otro desarrollo de personaje innecesario!
"""
#Entrada
"""
Se te dará una lista N de nombres, los cuales son los amores de Bodoque, y dependiendo de la cantidad 
de letras le dirás lo siguiente: 
"""
#Salida
"""
Dependiendo de la cantidad de letras, dirás lo siguiente:

Si el nombre tiene * 6 letras o menos, imprimirás: "No vale la pena".
Si el nombre tiene * 8 letras o mas, imprimirás:"Si aguanto otro desarrollo de personaje".
Si el nombre tiene ** mas de 6 pero menos de 8, imprimirás: "Dios no creo aguantar esta vez". .
"""

numeros = int(input()) #Cantidad de nombres

nombreslista = [] #Lista que contiene los nombres

for n in range(numeros): #dependiende de cuantos numeros
    Nombres = input() #son nombres
    nombreslista.append(Nombres) #.append agrega al final el nombre

H = 0

for x in nombreslista:
    if len(nombreslista[H]) <= 6:
        print("No vale la pena")
    else:
        if len(nombreslista[H]) >= 8:
            print("Si aguanto otro desarrollo de personaje")
        else:
            if len(nombreslista[H]) > 6:
                print("Dios no creo aguantar esta vez")
    H += 1 #a cada final de bucle le suma uno