#Descripcion
"""
Un alumno desea saber si obtendrá su premio al estudio en el presente semestre por lo que captura en un programa 
sus 6 calificaciones, en donde calcula su promedio y determina si obtiene el premio por un promedio mayor a 9.5.
"""
#Entrada
""" 
Recibirás en seis líneas diferentes un número con decimales Ci
 donde para la i
sima línea será la calificación para la materia i 
"""
#Salida
""" 
Deberas mostrar "Gana Premio :)" en caso 
que su promedio para las seis materias sea mayor a 9.5. En caso contrario "No Gana Premio :(".
"""

Nota1 = float(input())
Nota2 = float(input())
Nota3 = float(input())
Nota4 = float(input())
Nota5 = float(input())
Nota6 = float(input())
Notas = (Nota1 + Nota2 + Nota3 + Nota4 + Nota5 + Nota6) / 6
print(Notas)
print(type(Notas))
if (Notas > 9.5):
    print("Gana Premio :)")
else:
    print("No Gana Premio :(")
    
#poq 78.95???