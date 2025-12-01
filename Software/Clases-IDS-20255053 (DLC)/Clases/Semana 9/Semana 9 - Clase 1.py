#los 'set' no permite que se repita valores
#vamos a crear nuestro primer set
my_set = {"rojo","verde","negro","azul","rojo","azul"} #el uso principal del set es para generar una lista de valores no repetibles
#Tener en cuenta que azul no es lo mismo que Azul, el set lo contaria como otro
print("{'rojo'","'verde'","'negro'","'azul'","'rojo'","'azul'}","Esta seria la lista antes del set.")
print(f"{my_set} Es la lista ya modificada.")
print(f"siempre y cuando se use las llaves sera {type(my_set)}")
print("Los sets sirven mucho para cuando tienes muchos repetidos y solo quieres ver uno de cada uno")
#IMPORTANTE recordar que los sets se ponen con {} al declarar una variable

print("")
print("--------------------------------------------------------------------------------------------------")
print("")
#toda esta dih es nomas para a la hora de printear todo el desmadre se vea mas ordenadito y ya eso

mi_mascota = {
    "tipo":"perro", #Lo que hace los : en este caso cacho que lo asocia tipo en este caso 'perro' esta asociado con 'tipo'
    "nombre":"Harry", #'clave':'valor' que tiene asignado (no necesesariamente tiene que ser str)
    "edad":4, #clave:valor = item
    "personalidad":"good boy"}
#Esto es un ejemplo de diccionario
print("En listas y tuplas SI IMPORTA el orden")
print(type(mi_mascota))

regys_mascota = {
    "edad": 4,
    "nombre": "Harry",
    "personalidad": "good boy",
    "tipo": "perro"
}

son_iguales = mi_mascota == regys_mascota
print(f"Son las dos mascotas iguales?: {son_iguales}") #Si es true es pq los items creados (tipo,nombre,edad,personalidad) tiene el mismo valor

print("")
print("--------------------------------------------------------------------------------------------------")
print("")

birthday = {
    "Alice": "Apr 1",
    "Bob": "Dec 12",
    "Carol": "Mar4"
}
print(f"Lista og {birthday}.")
birthday["Carol"] = "Sep 12" #Esto lo cambia a sep 12 antes de printearlo aunque antes era Dec 12
print(birthday["Bob"]) #esto extrae la info de Bob ya que la tipica de [0] en librerias no cuela eh
print(f"Aqui la lista con la fecha de bob cambiada {birthday}.")
del birthday["Bob"]
print(f"Aqui la lista sin bob, fok bob{birthday}.")

for person, date in birthday.items():
    print(f"El cumpleaños de {person} es el dia {date}.")

print("")
print("--------------------------------------------------------------------------------------------------")
print("")