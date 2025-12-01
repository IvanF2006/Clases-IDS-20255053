#Modulo de logicas para el sistema

#Impor de modulo de datos
import modulo_datos1 as dat

def registrar_estudiante(): #Esto es para crear la funcion de "Registrar un estudiante"
    """Funcion que valida y registra estudiante"""
    while True:
        
        carnet_i = input("Digite el numero de carnet: ") #Carnet que ha sido recibido desde un input
        existe = "No"
        
        for e in dat.estudiantes: #cada una de las veces que haya una e revise la onda
            if e["carnet"] == carnet_i:
                existe =  "Si"
        
        if len(carnet_i) >= 6 and len(carnet_i) <= 10 and existe == "No":
            break
        else:
            print("El largo debe ser mayor a 5, menor que 11 Y no tiene que ser el mismo.")
                
    while True:
        nombre_i = input("Digite el nombre del estudiante: ")
        if len(nombre_i) > 1:
            break
        else:
            print("El largo del nombre debe ser al menos 2.")
    
    while True:
        apellido_i = input("Digite el apellido del estudiante: ")
        if len (apellido_i) > 1:
            break
        else:
            print("El largo del apellido debe ser al menos 2.")
    
    dat.estudiantes.append({
        "carnet": carnet_i,
        "nombre": nombre_i,
        "apellido": apellido_i
    })
    
    
    
    
    
    
    
    

def inscribir_en_curso():
    """Funciona para registrar alumnos por curso"""