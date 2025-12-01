#el uno y el dos que son los facilitos
agente = "encargado"
platillo = []
precios = []
registrado = False #es la cuestion que da acceso al resto del codigo ya que si esta false no es el agente registrado

if registrado == False:
    nombre_de_agente = input("Nombre del agente:" )

    while nombre_de_agente != "encargado":
        print("Agente no registrado")
        print("Favor ingrese el nombre del agente")
        nombre_de_agente = input("Nombre del agente:" ) #aqui se repite el bucle hasta que se meta el registrado vea y aha

registrado = True #aha y al estar registrado te da todas las opciones

#el resto cffffffffff
while registrado == True: #bucle para todas las opcione y tal
    opciones = int(input("1.Agregar platillos, 2.Consultar platillos y precios, 3.Colocar un pedido, 4.Salir: ")) #lista con las opciones
    
    if opciones == 1:
        
        creacion_de_platillos = input("Ingrese el nombre del platillo a crear: ")
        precio_de_platillo = float(input("Ingrese el precio del platillo a crear: "))
        
        if creacion_de_platillos[0] == "" or creacion_de_platillos[0] == " ": #aqui como en el ejercicio ese donde verificamo si pone espacio o nada ps printea que no ha puesto nada el wn
            print("No agregaste ningun platillo") #on another note tenia lo mismo para el precio pero tengo el conflicto este de float y str so
        if precio_de_platillo < 0: #pa que no haya ningun platillo con precio negativo y esta tambien aqui antes para que NO se printee
            print("El precio no puede ser negativo")
        else:
            platillo.append(creacion_de_platillos)#printe ya listos y el append esta pa aha implementarlos a la lista
            precios.append(precio_de_platillo)


    elif opciones == 2:
        
        if len(platillo) == 0: #si no hay nada escrito ps que no hay plato va y sino ps que printee
            print("No has consultado ningun platillo")
        else:
            print(platillo)
            print(precios)

    elif opciones == 3:
        
        platillo_elegido = input("Coloque el plattilo a pedir: ")
        
        ubicacion_de_platillo = platillo.index(platillo_elegido) 

        print(f"Usted ha elegido {platillo[ubicacion_de_platillo]} con un precio de ${precios[ubicacion_de_platillo]}")
        
    elif opciones == 4:
        registrado = False














#Hola alvin :) CREO que asi se hace el codigo pero si no ni modo