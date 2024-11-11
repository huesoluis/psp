import random
import time

# Generar un array de 1000 números aleatorios entre 1 y 10000
#array = [random.randint(1, 100000) for _ in range(5000000)]
array = [random.randint(1, 5000) for _ in range(1000)]

# Iniciar la medición del tiempo
start_time = time.process_time()

# Calcular el valor máximo del array
max_value = max(array)

# Finalizar la medición del tiempo
end_time = time.process_time()

# Calcular el tiempo total
total_time = end_time - start_time

# Mostrar el resultado
print(f"El valor máximo del array es: {max_value}")
print(f"Tiempo total para calcular el valor máximo: {total_time:.6f} segundos")

