#Descripcion
"""
Ves a Ivan conectado en el Facebook y quieres saludarlo pero para poder ademas presumirle que tu ya sabes C/C++ 
realizas un programa que lo salude cada ves que lo veas conectado. 
"""
#Entrada
"""
Una unica y simple entrada en la que dira 'conectado' o 'desconectado'. 
"""
#Salida
"""
Imprimir Ola Ivan si esta conectado e imprimir Ol.. si no. 
"""

estado = input()

while estado == "Conectado".lower():
    print("Ola Ivan")
    estado = "Esta conectado"
if estado != "Esta conectado": #Se refiere a que si estado no esta conectado va printear Ol..
    print("Ol..")