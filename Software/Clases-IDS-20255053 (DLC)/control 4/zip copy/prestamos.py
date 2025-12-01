'''3. Préstamos
Cada préstamo guarda:
•	carnet_estudiante
•	codigo_libro
•	fecha (string ingresada por el usuario, ej. “2025-03-10”)
3.	Registrar préstamo (25 puntos)
Crear función:
def registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos):
Debe:
1.	Pedir el carnet del estudiante
2.	Verificar que exista (si no, mostrar mensaje y no registrar)
3.	Pedir código del libro
4.	Verificar que exista
5.	Verificar que esté disponible
6.	Si está disponible:
o	Pedir fecha (string)
o	Guardar el préstamo
o	Marcar el libro como no disponible

'''
def registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos): #bueno agarramos las listas para usarlas aca ya que el prestamo se usa todo basciamente
    #primero la lista de libros
    pedirlibro = input("Ingrese el codigo del libro: ")
    
    libro_estado = False #el estado del libro al principio queda false pq aha aun no tiene ninguno ingresado
    for l_e in lista_libros:
        if l_e["Codigo: "] == pedirlibro: #pide el codigo del libro y si es el mismo que se inputio pasa a su estado a True
            libro_estado = True
            libro = l_e #hace que en el diccionario libro sea l_e que aha es para ver si esta disponible o no
            break #El break lo saque del main de alvin y bueno eso
    if libro_estado == False: #Y bueno si se mantiene false es porque no existe o quiza se escribio el codigo mal pero ni modo
        print("El libro no existe")
        return
    if libro["Disponibilidad: "] == False: #Y bueno si ya esta cachado el libro y es false pues no esta disponible
        print("Libro no disponible")
        return
    
    #segundo la lista de estudiantes
    pedircarnet = input("Ingrese el carnet del estudiante: ") #casi que la misma explicacion que la de los libros
    
    estudiante_estado = False
    for e_e in lista_estudiantes: #ve si el estado del estudiante existe verificando
        if e_e["Carnet: "] == pedircarnet: #entonces compara el codigo de la libreria del estudiante con la inputiada aqui
            estudiante_estado = True
            estudiante = e_e #confirma que el estudiante este y lo mete al diccionario y tal
            break
    
    if estudiante_estado == False: #bueno lo mismo de que si no existe el estudiante pues ni modo
        print("No existe el estudiante")
        return
    
    else:
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ") #ya cuando todo ese mombo termina te pregunta para ingresar la fecha en ese formato pq aha es el del paper 
        
        prestamo = { #la libreria del prestamo
            "Carnet: ": pedircarnet,
            "Codigo: ": pedirlibro,
            "Fecha: ": fecha
        }
        
        lista_prestamos.append(prestamo) #añade los prestamos a la lista y aha
        libro["Disponibilidad: "] = False #y cambia su disponibilidad una vez ya este en uso el libro
        
        print("Prestamo registrado")
        
def mostrar_prestamos(lista_prestamos): #muestra los prestamos
    if lista_prestamos == []: #si no hay no hay :VVVVVVVV
        print("No hay prestamos")
    else:
        for prestamo in lista_prestamos: #ya luego printea en el formato de carnet/codigo/prestamo(fecha)
            print(prestamo["Carnet: "], prestamo["Codigo: "], prestamo["Fecha: "])
            
#si la documentacion no esta muy buena perdon ahi profe
""" 
⬤▅▇█▇▆▅▄▄▄▇ 󠀀
"""