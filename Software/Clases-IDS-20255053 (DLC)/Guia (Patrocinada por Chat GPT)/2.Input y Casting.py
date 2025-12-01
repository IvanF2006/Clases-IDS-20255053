#Nivel 1: Pide tu nombre y muestra un saludo.
nombre = str(input("Cuales tu nombre?: "))
print(f"Hola {nombre}.")

#Nivel 2: Pide un número y muestra su triple.
pregunta_numero = int(input("Ingresa un numero: "))
print(pregunta_numero*3)

#Nivel 3: Pide tres precios y muestra el total.
precio_uno = float(input("Ingresa el primer precio: "))
precio_dos = float(input("Ingresa el segundo precio: "))
precio_tres = float(input("Ingresa el tercer precio: "))

print(f"El precio total es ${precio_uno + precio_dos + precio_tres}.")

#Nivel 4: Pide el año de nacimiento y muestra si ya cumpliste años este año (usa condicional).
año_nacimiento = int(input("Ingresa el año en el que naciste: "))
mes_nacimiento = int(input("Ingresa el mes en el que naciste: "))
mes_actual = int(input("Ingresa el mes actual: "))

if mes_actual >= mes_nacimiento:
    print("Ya cumpliste años")
else:
    print("Aun no cumples años")


#Nivel 5: Pide dos números decimales y muestra el promedio con dos decimales.
numero1 = float(input())
numero2 = float(input())
promedio = (numero1 + numero2) / 2

print(f"El promedio es: {promedio:.2f}")