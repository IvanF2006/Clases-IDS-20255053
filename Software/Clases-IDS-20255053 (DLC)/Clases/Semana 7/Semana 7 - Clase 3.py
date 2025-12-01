#Mas o menos como introduccion del if y tambien de que son como una lista de estas que vi en el cole
nota = int(input("Ingrese la nota: "))

if nota == 10:
    print("E")
else:
    if nota > 7:
        print("MB")
    else:
        if nota > 5:
            print("B")
        else:
            if nota > 3:
                print("R")
            else:
                print("M")
                
#Ejercicio
monto = float(input("Digite el monto: "))
tipo = input("Ingrese el tipo (Local/Export)")
impuesto = 0

if tipo.lower() == "local":
    if monto > 500:
        impuesto = 0.1
    else:
        if monto > 200:
            impuesto = 0.08
        else:
            if monto > 50:
                impuesto = 0.06
            else:
                impuesto = 0
elif tipo.lower() == "exportacion": #elif es una combinacion entre else e if (muy cheto la verdad) y se pone para cualquier otra cosa pero cumpliendo lo que pide
    if monto > 500:
        impuesto = 0.14
    else:
        if monto > 200:
            impuesto = 0.12
        else:
            if monto > 50:
                impuesto = 0.10
            else:
                impuesto = 0
else:
    print("Esta mal en algo")

print(f"El impuesto a pagar de tipo {tipo} por venta de {monto:,.2f}")
print(f"es de {monto*impuesto:,.2f}")
    
"""
osea queiro aclarar que el elif es un else con un if adentro en el sentido que si else if cachai osea si no se cumple
lo contrario + una pregunta que seria el if, es una pregunta en el else 
"""