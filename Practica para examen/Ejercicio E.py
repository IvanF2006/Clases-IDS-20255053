Nota1 = float(input())
Nota2 = float(input())
Nota3 = float(input())
Nota4 = float(input())
Nota5 = float(input())
Nota6 = float(input())

Lista = [Nota1 , Nota2 , Nota3 , Nota4 , Nota5 , Nota6]
Suma_Total = (Nota1+Nota2+Nota3+Nota4+Nota5+Nota6)
print(f"Maximo: {max(Lista):.2f}")
print(f"Minimo: {min(Lista):.2f}")
print(f"Diferencia: {max(Lista) - min(Lista):.2f}")
print(f"Suma: {Suma_Total:.2f}")
print(f"Promedio: {Suma_Total / len(Lista):.2f}")