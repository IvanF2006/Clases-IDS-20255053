#Clase 3 de la semana 3 (de la primera que fue grabada type shi)

"""
ponele que aha los datos en python son como los ingredientes de una receta y cada uno
de estos aporta y tal
"""

variable1 = 123

#Perseverancia de datos
"""
basicamente el teach dice de como los datos cobran vida ponele siempre y cuando el codigo
se este ejecutando pq cuando se deja de ejecutar mueren alv :Vvv y bueno tambien habla de 
cuando ejecutas un codigo esta como unos tres doritos >>> dichos doritos implican que vsc
esta esperando a que se ejecute dicho codigo o al menos asi entiendo
"""

valor = variable1 + 6

"""
algo que muy IMPORTANTE que explica el teach imo es que si quieres como interactuar
con una variable pero la variable esta despues de dicha interaccion pues no va funcionar
ya que la variable tiene que existir o en este caso estar escrita y ser programada antes
de que la variable pueda tener algun tipo de interaccion, lo cual suena muy obvio pero a 
la larga puede pasar, ah y a esto se refiere el teach cuando dice la cuestion de 
PERSEVERANCIA DE DATOS, y bueno para guardar datos de forma permanente fuera de vsc
seria de usar archivos tipo txt o excell type shit

Y bueno solo para ser super claro con esta cuestion basciamente puedes hacer esto
Variable1 = 123 ///luego/// valor = Variable1 + 6
pero NO puedes hacerlo al revez pq aha es muy estupido sumar una variable que
aun no esta definida por ende aun no exisite
valor = Variable1 + 6 ///luego/// Variable1 = 123 esto NO SE PUEDE Y DA ERROR
y bueno aclarar tambien que cuando se deja de ejecutar el codigo las variables tambien

Y bueno ya hablando mas del tema de la creacion de variables basicamente del lado izq
le das como el nombre y del lado derecho del = le estas asignando un valor que va tener
ese nombre basicamente
"""

#variablename = value

"""
Y bueno hay unas cuantas como mini reglas con el tema de las variables y es que a la
hora de crear variables ps no puedes usar if,for,while,etc ya que ya son palabras que 
estan reservadas para el mero python so dont use em, luego tienen que si o si comenzar
con una letra o guion bajo y si se quiere usar un espacio que se use un guion bajo
ya despues se recomienda documentar cada variable con el # y/o usar nombres self
explanatories asi es mas facil leer el spagueti code que uno ha hecho
"""

"""
Tipos de datos 
        +Numeros
            -Enteros
            -Booleanos (Basicamente son los True[1]/False[0])
            -Numeros reales
            -Numeros complejos
            -Fracciones y decimales
        +Secuencia Inmutables
            -Strings, Tuplas y Bytes
        +Secuencia Mutables (Ejemplo: 1,3,6,10,4 /// Y bueno la diferencia entre las
        Mutables con las Inmutables es que las Mutables se les puede cambiar o 
        modificar dichas secuencias en cambio las Inmutables asi como esta su secuencia
        asi se queda y na que hacerle)
            -Listas y arrgelos de Bytes
        +Fechas
        +Numeros parte 2 la venganza de los puntos
            -Enteros (int) [Ejemplo: numeros enteros wn]
            -Flotantes (float) [Ejemplo: numeros decimales]
"""

#Ejemplo de enteros
edad = 30
numero_casas = 5

#Ejemplos de flotantes
pi = 3.141592653589793
temperatura = 25.5

usuario = "Toño," #Cuando son casos como este si se pueden usar simbolos especiales

year = 2025 

"""
Tambien el teach recomienda mejor ahorrarse el rollo y usar mejor el
ingles pq no solo es objetivamente el mejor lenguaje sino tambien es bastante
util a la hora de programar en absolutamente todo a no ser que tengas altos
problemas mentales y uses PSeInt
"""

grad = year + 5

print(grad)
print(year)
print(temperatura)
print("pi") #Y aha tilin aqui vemos un ejemplo donde si esta en "" es texto
print(pi) #Y aqui como no esta con "" es el valor que le dimos anteriormente

nota = 6.7
aprobacion = 4.1

estado1 = nota > aprobacion

print(estado1)

"""
Bueno asi rapidito aqui una lista de los operadores (los caules son los simbolos
para programar y toda esa shit ugwim)
    [+]         Addition/Suma                               1+1=2
    [-]         Subtraction/Resta                           10-1=9
    [*]         Multiplicacion                              3*5=15
    [/]         Division                                    10/5=2
    [%]         Modulus (remainder after division)          11%5=1
    [**]        Exponente                                   3**2=9
    [//]        Floor division                              11//5=2
    [<]         Less than
    [<=]        Less than or equal to
    [>]         Greater than
    [>=]        Greater than or equal to
    [==]        Equal to
    [!=]        Not equal to
    [is]        Object identity
    [is not]    Negated object identity
"""
estado2 = nota == 8
print(estado2)

estado3 = nota != 6.9
print(estado3)

#Pongo estos prints para separar los codigos estos y tal type shi
print("///")
print("///")
print("///")

edrad = 20                                  #Variable tipo entero
tempreratura = 67.41                        #Variable tipo flotante
tempreratura_entera = int(tempreratura)     #aqui lo cambias a numero entero
nombrer = "41unc"                           #Variable tipo numerico

print(tempreratura_entera)

#fin de la clase