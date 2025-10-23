"""
entonces ponele que aha print es como para salida he input es para
entrada y type shi asi super niche y tuff
"""

mrsixseven = input("bro: ")
print(f"bro " + mrsixseven)

"""
Bueno aqui arriba va ^^^ me fui un poco fuera del ejemplo pero aha
para hacer que print tenga como un texto y luego una variable aha se usa
como ese combo va de la f el texto + la variable y ya solo eso queria
como documentar vea tambien lo del inputn nomas aqui se usa para poner
lo que se quiere poner
"""

#Ejemplo de clase btw de como repaso va
ItemIngresar = input("Ingrese el item: ")
print(f"El item ingresado es {ItemIngresar}")

"""
Bueno esta es otra forma de hacerlo ^^^ y creo que es la forma correcta
no se pensaba en mi mente que era mejor con el mas pero aha lwk es mas meta
las llaves {}
"""

"""
va algo importante y basico que aha ya deberia de quedar claro pero 
solo por si las moscas y es que las palabras y CREO que todo lo que se
le considera texto se le llama STRINGS o cadena de caracteres pero ese
termino es mas niche y aha ya tenemos varios ejemplos como el de
    usuario = "profe"
    print(type(usuario))
    print(type(usuario) is str) /// el str aha siendo el codigo pa string
    print(type(usuaario) is int) /// el cual no es pq int es pa numeros
"""

#Ejemplo de clase de como poner espacios a la hora de printear
nombre = "Labubu"
inicial = "L"
apellido = "Mango"
nombrecompleto = nombre + inicial + apellido
print(nombrecompleto)
nombrecompletoSp = nombre + " " + inicial + " " + apellido
print(nombrecompletoSp)

"""
Entonces aha este ejemplo ^^^ basicamente es que aha a la hora de printear
no te va dar con los espacios entonces le sumas los espacios y ya un poco
obvio imo pero supongo que eso te va poco a poco dando esa forma de pensar
como de software type shi
agregar que los espacios cuentan como caracteres y eso
"""

#Ejemplo del uso len y cuestiones de los caracteres
s1 = ""
s2 = " "
s3 = "6 7"
print(len(s1))
print(len(s2))
print(len(s3))

"""
Aqui nomas usa len que entiendo yo que lo unico que hace es que te da un
numero de cuantos caracteres hay entre las comillas y ya eso, la logica
iria algo asi
    ABCDE
    01234 <- como los va contando la compu y bueno es por eso que el profe
             dice que empecemos contando el 0 y aha eso
"""

#Otro ejemplo de len y aha
labubu_dih = "Longahhhhhhhh"
print(len(labubu_dih),"cm") #uso de coma que ni idea como funciona lol
#antes del input se le pone int para que lo cache como numero
dihbubu = int(input("Tungtungtung sahur: "))
print(labubu_dih[dihbubu])
print(labubu_dih[0:4]) #los dos puntos se consideran como un "x hasta y"

"""
En la linea 78 se pone en el [0:4] se pone cuatro pq por una bs de mate
se tiene que poner una mas de la que quieres agarrar pq aha empieza desde
0 pero no cacha el ultimo que agarra, oh bueno viendolo de una forma mas
facil de entender el numero que le dices despues del primero es el numero
donde va a terminar, por ejemplo digo que empiece desde 0 va y termine en 4
    Longahhhhhhhh
    0123456789 lwk no se como se cuenta pasado el 9 pero aha
cuestion que como le digo que empiece desde 0 lo cuenta type shi va y luego
para en el 4 y no lo cuenta pq ahi es donde para y ya eso

oh bueno otra ofrma de interpretarlo
    -> numero que quiero que incluya :(hasta) numero que no quiero que incluya <-
""" 

print(labubu_dih [0:9:2]) #el segundo : ya es como la cantidad de steps

"""
osea muy bs siento esta parte pero x, osea el primer numero es desde que
empieza contando ese numero de ahi va el primer : que representa hasta que
numero va contar y dicho numero lo va ignorar y luego el tercer : implica
la cantida de pasos que va saltar o contar osea cada dos pasos va contar
un numero type shi osea primero si segundo no, saltos de cada dos

sino queda claro mira el ejemplo y siento que con contar las letras con las
manos he ir bajando los dedos se facilita comprender como funciona esta shi
"""