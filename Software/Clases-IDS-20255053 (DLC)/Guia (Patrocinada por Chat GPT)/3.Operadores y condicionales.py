#Nivel 1: Pide un número e indica si es positivo o negativo.
numero = int(input("Ingresa un numero: "))

if numero > 0:
    print("Numero positivo.")
else:
    print("Numero negativo.")

#Nivel 2: Pide dos números e imprime el mayor.
numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa un numero: "))

if numero1 > numero2:
    print(numero1)
else:
    print(numero2)

#Nivel 3: Pide una edad y muestra si puede votar.
edad_votador = int(input("Ingresa tu edad: "))

if edad_votador > 18:
    print("Puedes votar")
else:
    print("No puedes votar")
    
#Nivel 4: Pide tres números y muestra el menor.
primer_numero = int(input("Ingresa el primer numero: "))
segundo_numero = int(input("Ingresa el segundo numero: "))
tercer_numero = int(input("Ingresa el tercer numer: "))

numero_lista = [primer_numero,segundo_numero,tercer_numero]
print(f"El numero menor es: {min(numero_lista)}.")
