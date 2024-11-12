#código c23_vmaximo.py
import threading
import random

# Generar un array de 100 enteros aleatorios entre 1 y 1000
array = [random.randint(1, 1000) for _ in range(100)]

# Variables para almacenar los máximos parciales
max_result = [0, 0]

# Función para encontrar el máximo en una porción del array
def find_max(start_index, end_index, index):
    max_value = array[start_index]
    for i in range(start_index + 1, end_index):
        if array[i] > max_value:
            max_value = array[i]
    max_result[index] = max_value

# Calcular los índices para dividir el array
mid_index = len(array) // 2

# Crear los hilos
thread1 = threading.Thread(target=find_max, args=(0, mid_index, 0))
thread2 = threading.Thread(target=find_max, args=(mid_index, len(array), 1))

# Iniciar los hilos
thread1.start()
thread2.start()

# Esperar a que los hilos terminen
thread1.join()
thread2.join()

# Obtener el máximo global
global_max = max(max_result)

print(f"El máximo valor del array es: {global_max}")
