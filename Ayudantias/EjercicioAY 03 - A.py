LENN = int(input())
IDN = int(input())
LCJ = int(input())
ISND = int(input())
tupla = (LENN, IDN, LCJ, ISND)
nombres = ("LEN", "IDN", "LCJ", "ISND")
print(nombres[tupla.index(max(tupla))])
"""
el codigo max busca el valor maximo
el split hace que vaya de forma separada
"""