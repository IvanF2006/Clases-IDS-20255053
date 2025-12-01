def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = 67

print(f"¿El número {numero} es primo?: {es_primo(numero)}")

# Mostrar la tabla de multiplicar del 67
print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Generar una lista de múltiplos de 67 hasta 670
multiplos = [numero * i for i in range(1, 11)]
print(f"\nLos primeros 10 múltiplos de {numero} son: {multiplos}")