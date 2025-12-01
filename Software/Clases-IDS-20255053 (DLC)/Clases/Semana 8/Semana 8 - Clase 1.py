numeros = [1,2,3,4] #LISTA
print((len(numeros))) #Len -> cuantos elementos tiene la LISTA

palabra = "Aulas"
print(len(palabra))

for x in numeros: #Como tiene 4 elementos dice Hola 4 veces, eso es lo que hace el x
    print("Hola")
 
print("-------------------------") #Esto esta solo para no confundirme y ya

for x in palabra:
    print("Hola")

print("-------------------------")

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

for x in dias[2]:
    print(x)
 
print("-------------------------")
    
for x in dias:
    print(x[:2])
    
print("-------------------------")

print(range(1,10)) #agarra desde uno hasta cero (argumento uno, argumento dos)//(donde va iniciar, donde va terminar)
#recordatorio que e el ultimo no se cuenta tpye shi

print("-------------------------")

for i in range(10):
    print(i)
    
print("-------------------------")

#Inicion/Fin/Saltos , como en las LISTAS
for i in range(0,10,2):
    print(i)
    
print("-------------------------")

personas = ["Ana","Luis","Luisa"]
for p in personas:
    print(p)
    for l in p:
        print(l)
        
print("-------------------------")

valores = [[1 ,3, 6],
           [2, 7, 4],
           [6 ,5 ,9],
           [1,10,20]]

mayores = []
minimi = int(input("digite el minimo: "))
for v in valores: #accedo a cada uno de los elementos
    for valorcito in v: #y aqui cada uno de los elementos de cada uno de los elementos
        if valorcito > minimi: #se ejecuta solo si es mayor al numero inputeado
            mayores.append(valorcito) # .append es un metodo de LISTA que agrega hasta el final
print(mayores)