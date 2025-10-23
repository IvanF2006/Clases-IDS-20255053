correo = input()
condicion1 = correo.count("@") == 1
arroba = correo.index("@")
conodicion2P1 = arroba >= 3
conodicion2P2 = (len(correo)-arroba) > 3
condicion3 = correo.count(" ") == 0
condicion4 = correo.count(".") >= 1
condicion5P1 = correo[0] != "."
condicion5P2 = correo[-1] != "."

condicionFINAL = condicion1 & conodicion2P1 & conodicion2P2 & condicion3 & condicion4 & condicion5P1 & condicion5P2
print(condicionFINAL)