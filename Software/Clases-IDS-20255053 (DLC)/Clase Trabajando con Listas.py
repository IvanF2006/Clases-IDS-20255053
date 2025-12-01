#Semana 7

"""
#RESOLUCION DEL PARCIAL
#Ejercicio 1
num1 = int(input())
num2 = int(input())
print(num1 == num2)

#Ejercicio 2
Num1 = int(input())
Num2 = int(input())
print(Num1 % Num2 == 0)

#Ejercicio 3
palabra = input()
letra = input()
print(palabra[-1].lower() == letra.lower())
print(palabra)

#Ejercicio 4
Palabra = input()

print(Palabra[::-1].lower() == Palabra.lower())
print(Palabra)

#Ejercicio 5
PalabrA = input()
LetrA = input()

print(PalabrA.count(LetrA) > 0)
print(LetrA.lower in PalabrA.lower) #in busca como que aha que este adentro de eso ig

#Ejercicio 6
numero = float(input())
print(numero == int(numero))

-is o is not es para comparar tipo de datos
-valores es para numeros asi


#Ejercicio 7 (el del DUI)
DUI = input()
cond1 = len(DUI) == 10
cond2 = DUI[8] == "-"
print(type(int(DUI[-1]) is int)) #is es para comparar tipos NO valores

#Fin de ejercicios parcial
"""
lista = [1,2,"tres",["ene","feb","mar"]]
print(len(lista))
print(lista)
print(lista[2][2:].upper()) #upper es mayuscula y los dos puntos de [2:] significa que va a empezar desde 2 hasta el final
#como obtengo la a de marzo
print(lista[3][2][1])

numero = ["uno","dos","tres"]
print(numero)
numero = numero + ["cuatro","cinco","seis"]
print(numero)
numero[2] = "three"
print(numero)