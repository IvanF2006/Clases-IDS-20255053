#STRING
#TUPLA
#LISTA
numeros = [0,1,2,3,"uno","Dos","tres"]
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])
print(numeros[5])
print(numeros[6])
print(numeros.count("dos")) #preguntar a alvin que paso con lo de .lower

nombre = "Antonio"
print(nombre.count("n"))#Count en este caso cuenta las veces que aparece la letra n
print(nombre.lower().count("a")) #Aqui el .lower lo que hace es que hace todo minuscula asi contar la A mayuscula de antionio

Nombres = ["Ana","Antonio","Ana","Jose"]
print(len(Nombres[0]))
""" ^^^
Nombres = [0,1,2,3]
0 = ["Ana"]
1 = ["Antionio"]
2 = ["Ana"]
3 = ["Jose"]
"""
#Cual se puede decir que es la lista, tupla y string

print(Nombres.count("Luis"))
print(Nombres.count("a"))
print(Nombres[0].count("a")) #aqui el [0] esta sacando el "Ana" y ahi esta contando las a MINUSCULAS que tiene
print(Nombres[0].lower().count("a")) #lo mismo pero esta vez haciendo todas MINUSCULAS
r_a = 0
r_a = r_a + Nombres[0].lower().count("a")
r_a = r_a + Nombres[1].lower().count("a") # segundo componente
r_a = r_a + Nombres[2].lower().count("a")
r_a = r_a + Nombres[3].lower().count("a")
print(r_a) #r_a al final lo que va haciendo es sumar todos los r_a =
""" ^^^
eehhhhh es el codigo para hacer listas y que en la lista countear y luego sacar el resultado de lo caunteado y tal 
"""
NOmbres = ["Ana","Antonio","Paulina","Jose"]
print(NOmbres)
NOmbres[2] = "Pablo"
print(NOmbres)
NOmbres.append(input("Ingrese el nuevo nombre: ")) #aqui seria como agregando uno tu mismo y tal
NOmbres.append("Hazel") #.append es como agregar al final una cuestion
print(NOmbres)
NOmbres.insert(3,"Sebas") #lo que hace el 3 e que el segundo cambia a ser seba
print(NOmbres)
NOmbres.remove("Sebas")
print(NOmbres)
NOmbres.insert(int(input("Indique el indice: ")), input("Nombre: "))
print(NOmbres)
nombre_borrado = NOmbres.pop(int(input("Indice a borrar: "))-1)
NOmbres

#Bueno pedirle codigo a Alvin que la lie parda
#Tengo en el telefono unas fotillos de unas cuestiones IMPORTANTEs