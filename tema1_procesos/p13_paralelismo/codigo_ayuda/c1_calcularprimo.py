import random
import time

# Función para determinar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generar un array de 1000 números aleatorios entre 1 y 10000
array = [random.randint(1, 10000000) for _ in range(500000)]

# Iniciar la medición del tiempo
start_time = time.time()

# Filtrar solo los números primos en el array
primos = [num for num in array if es_primo(num)]

# Calcular el número primo mayor
if primos:
    max_primo = max(primos)
else:
    max_primo = None

# Finalizar la medición del tiempo
end_time = time.time()

# Calcular el tiempo total
total_time = end_time - start_time

# Mostrar el resultado
if max_primo:
    print(f"El número primo mayor del array es: {max_primo}")
else:
    print("No se encontraron números primos en el array.")
print(f"Tiempo total para calcular el número primo mayor: {total_time:.6f} segundos")

