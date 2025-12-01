#Nivel 1: Crea una variable con tu color favorito y muéstralo.
color_favorito = "Verde"
print(color_favorito)

#Nivel 2: Declara tres variables (nombre, edad, país) y muestra una oración completa.
nombre = "Carlos"
edad = 26
pais = "Peru"

print(f"Mi nombre es {nombre}, tengo {edad} y vivo en {pais}.")

#Nivel 3: Crea una variable año_nacimiento y calcula tu edad con base en 2025.
año_de_nacimiento = int(input())
calculo_de_edad = (2025 - año_de_nacimiento)

print(f"Tienes {calculo_de_edad} años.")

#Nivel 4: Usa comentarios para explicar qué hace tu programa que calcula el área de un cuadrado.
area = int(input()) #aqui el usuario ingresa el lado del cuadrado para calcular el area
calculo_de_area = area*area #se calcula el lado por lado que equivale al area

print(calculo_de_area) #muestra el resultado

#Nivel 5: Crea un programa que combine texto y operaciones matemáticas en un solo print()
print(f"El resultado de 2 + 4 es: {2 + 4}")