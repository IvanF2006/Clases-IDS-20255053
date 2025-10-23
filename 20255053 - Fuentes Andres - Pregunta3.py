#Entrada: 2 Cadenas de caracteres
#Salida: True/False
#Restricciones: entre 1 y 1000

"""
Programar = input()

pro = input().count(Programar)

r = Programar == pro

print(r)
"""
#^^^ experimento fallido #1

"""
cadena_de_caracter_1 = str(input())
cadena_de_caracter_DOS = str(input().count(str(len(cadena_de_caracter_1))))

termina = cadena_de_caracter_1[0::-1] == cadena_de_caracter_DOS
print(termina)
"""
#^^^ experimento faliido #2

A = (str(input()[-1::]))
a = str(input())

validar = A[0::1000] == a[0::1000]

print(validar)

#si o si tiene que estar bueno