"""
•	Pide al usuario su nombre usando input() y muéstrale un saludo personalizado.
"""
nombre = input("Ingresa tu nombre: ")
print("Bienvenido/a/e",nombre)

"""
•	Pide al usuario su edad y muestra un mensaje con el doble de esa edad. 
"""
edad = int(input("Ingresa tu edad: "))
print(edad*2,"Años duplicados")

"""
•	Pide dos números enteros al usuario, súmalos y muestra el resultado.
"""
numero1 = int(input("Ingresa tu primer numero a sumar: "))
numero2 = int(input("Ingresa tu segundo numero a sumar: "))
resultado = (numero1 + numero2)
print(resultado,"Es tu resultado")

"""
•	Pide al usuario un número decimal y muestra su mitad.]
"""
numerodih1 = float(input("Ingrea tu numero decimal: "))
print(numerodih1 / 2 ,"Es la mitad de tu numero decimal")

"""
•	Pide al usuario su año de nacimiento y calcula su edad (usando 2025 como año actual).
"""
anio_actual = 2025
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
print(anio_actual-(anio_nacimiento), "Es tu edad calculada.")

"""
•	Pide al usuario el precio de un producto y el número de unidades. Muestra el total a pagar.
"""
precioP = int(input("Ingrese precio de tu producto: "))
unidadesP = int(input("Ingrese la cantidad que deseas comprar: "))
print(precioP*unidadesP,"Dolares totales a pagar")

"""
•	Pide al usuario un número entero y muestra el cuadrado de ese número.
"""
numeroC = int(input("Ingresa numero a elevar: "))
print(numeroC**2)

"""
•	Pide al usuario dos números y muestra su promedio.
"""
numeroprom1 = int(input("Ingresa el primer numero a promediar: "))
numeroprom2 = int(input("Ingresa el segundo numero a promediar: "))
print(((numeroprom1)+(numeroprom2))/2)

"""
•	Pide al usuario su nombre completo y su edad, y muestra un mensaje con formato f-string como: Hola, Juan Pérez. Tienes 20 años.
"""
nombrecom = str(input("Ingrese su nombre completo: "))
edadcom = str(input("Ingresa tu edad: "))
print(f"Hola,{nombrecom}.Tienes {edadcom} años.")