#mostrar Y registrar libros 

# Ejercicio 1 

def registrar_libro(lista_libros):
    titulo = input("ingrese el titulo del libro: ")
    autor = input("ingrese el nombre del autor: ")
    
    Codigo = f"L{len(lista_libros)+1:03d}"
    
    libro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor, 
        "disponible": True
        
     }
    
    lista_libros.append(libro)
    print("Libro registrado con éxito. Código asignado:", codigo)
    
    #Ejercicio 4
    
    def mostrar_libros(lista_libros):
     if not lista_libros:
        print("No hay libros registrados.")
        return

    print("\n--- LISTA DE LIBROS ---")
    for libro in lista_libros:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"Código: {libro['codigo']} | Título: {libro['titulo']} | Autor: {libro['autor']} | Estado: {estado}")