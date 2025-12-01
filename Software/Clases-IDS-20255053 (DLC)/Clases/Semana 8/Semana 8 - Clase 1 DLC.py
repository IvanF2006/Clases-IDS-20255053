#En esta clase vemo el frikin while
inicio = 0
maximo = 5

while inicio < maximo:
    print("Saludo")
    inicio = inicio + 10 #esto e pa que no explote la wea

presupuesto = 1000
gasto = 0
while gasto <= presupuesto:
    compra = float(input("Digite el valor de compra: "))
    gasto += compra #es la forma fancy de escribir gasto + compra
gasto -= compra
print(gasto)

print("---------------------------")

estado = input()
while estado == "Conectado".lower:
    print("Hola Sebas")
    estado = input("Digite su estado: ")