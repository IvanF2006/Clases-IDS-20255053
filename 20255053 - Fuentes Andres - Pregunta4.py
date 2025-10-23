#Entrada: Una unica cadena de caracteres
#Salida: True or False
#Restricciones: entre 1 y 1000

Radar = str(input())

Ra = str((Radar[0:]))
Dar = str((Radar[::-1]))

radaR = (str(Ra) == str(Dar))
print(radaR)

#radaR = (len((Radar.count[0:]))) == (len(Radar.count[::-1]))
#print(radaR)