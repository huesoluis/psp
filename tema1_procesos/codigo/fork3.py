import os
import time
import random

# Crear un proceso hijo usando fork
pid = os.fork()

if pid > 0:
    # Este bloque es ejecutado por el proceso padre
    for i in range(1, 1112):
        # Añadimos un retraso aleatorio
        print(f"Padre (PID: {os.getpid()}), Iteración: {i}")
    time.sleep(2)  # Espera al final para evitar que termine antes del hijo
elif pid == 0:
    # Este bloque es ejecutado por el proceso hijo
    for i in range(1, 1112):
        # Añadimos un retraso aleatorio
        print(f"Hijo (PID: {os.getpid()}), Iteración: {i}")
    time.sleep(2)  # Espera al final para evitar que termine antes del padre
else:
    print("Error al crear el proceso hijo")

