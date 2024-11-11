import os
import time
import random

# Crear un proceso hijo usando fork
pid = os.fork()

if pid > 0:
    # Este bloque es ejecutado por el proceso padre
    # Añadimos un retraso aleatorio
    time.sleep(random.uniform(0.1, 1.0))
    print(f"Soy el proceso padre con PID: {os.getpid()}, el PID de mi hijo es: {pid}")
    time.sleep(5)  # Esperar 5 segundos antes de terminar
elif pid == 0:
    # Este bloque es ejecutado por el proceso hijo
    # Añadimos un retraso aleatorio
    time.sleep(random.uniform(0.1, 1.0))
    print(f"Soy el proceso hijo con PID: {os.getpid()}, el PID de mi padre es: {os.getppid()}")
    time.sleep(5)  # Esperar 5 segundos antes de terminar
else:
    print("Error al crear el proceso hijo")

