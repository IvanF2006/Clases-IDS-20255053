'''1. Libros
Guardados en una lista de diccionarios.
Cada libro tiene:
•	codigo (ej. L001, L002) — único
•	titulo
•	autor
•	disponible (True/False)
1.	Registrar libro (15 puntos)

Crear una función:
def registrar_libro(lista_libros):
La función debe:
•	Pedir título y autor
•	Generar el código del libro automáticamente (L001, L002, …)
•	Guardar un diccionario con la información
•	Marcar el libro como disponible inicialmente (disponible = True)
'''
def registrar_libro(lista_libros): #la definicion y tal para que se use en el main y aha aplica pa los otros dos pa asi no documentar ma
    
    titulo = input('Ingrese el titulo del libro: ').title() #Titulo del libro va 
    autor = input('Ingrese el autor del libro: ').title() #Su autor
    
    codigonumero = len(lista_libros) + 1 #chequea la cantidad de libros y le suma un uno asi empieza como en el ejemplo de las indicaciones
    codigoentero = f'L{codigonumero:03d}' #le pone los tres 0 pa que quede como el ejemplo
    
    libro = { #Diccionario del libro con todo su detalles
        "Titulo: ": titulo,
        "Autor: ": autor,
        "Codigo: ": codigoentero,
        "Disponibilidad: ": True
    }
    
    lista_libros.append(libro) #Lo termina appendiando a la lista
    
    
def mostrar_libros(lista_libros):#la definicion pa mostrar y aha lo mismo que la otra def aplica pa los otros tres
    if lista_libros == []: #Si no hay ningun libro pues imprime que no hay libros :V
        print("No hay libros")
    else:
        for libro in lista_libros: #Y bueno si lo hay saca cada dato del diccionario y los printea
            print(libro["Codigo: "], libro["Titulo: "], libro["Autor: "], libro["Disponibilidad: "])