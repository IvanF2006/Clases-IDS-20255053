usuarios = ["Ana","Carlos","Luis","Maria","Lorenzo"]
edades = [20, 19, 21, 22, 18]
frutas = ["mango","fresa","pera","sandia","piña"]

for posicion, usuario in enumerate(usuarios,start=1): #El enumerate esta para que les ponga index a los valores de la lista y darles valor
    print(f"{posicion} {usuario}") #El start hace que empiece desde ese valor
    
print("")
print("--------------------------------------------------------------------------------------------------")
print("")
    
for usuario, edad in zip(usuarios,edades): #El zip lo que hace es combina dos listas
    print(f"{edad} {usuario}")
    
print("")
print("--------------------------------------------------------------------------------------------------")
print("")

for usuario, edad, fruta in zip(usuarios, edades, frutas):
    print(f"El usuario {usuario}, con edad {edad}, le gusta {fruta}")