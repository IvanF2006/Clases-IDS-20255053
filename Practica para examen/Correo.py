"""
El correo contiene exactamente un @
Antes y después del @ debe haber al menos 3 caracteres
El correo debe contener al menos un punto
El correo no puede contener espacios
El correo no puede iniciar ni terminar con un punto
"""

correo = input()
c1 = correo.count("@") == 1
p_arroba = correo.index("@")
c2_1 = p_arroba >= 3
c2_2 = (len(correo)-p_arroba) > 3
c3 = correo.count(".") > 0
c4 = correo.count(" ") == 0
c5_1 = correo[0] != "."
c5_2 = correo[-1] != "."

mensaje = c1 & c2_1 & c2_2 & c3 & c4 & c5_1 & c5_2

print(mensaje)