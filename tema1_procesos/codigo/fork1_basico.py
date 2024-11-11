import os
import time

a=20
# Crear un proceso hijo usando fork
pid = os.fork()

if pid > 0:
    a=a+10
    # Este bloque es ejecutado por el proceso padre
    print(f"Soy el proceso padre con PID: {os.getpid()}, el PID de mi hijo es: {pid}")
    print(a)
    time.sleep(10)  # Esperar 5 segundos antes de terminar
elif pid == 0:
    a=a+30
    # Este bloque es ejecutado por el proceso hijo
    print(f"Soy el proceso hijo con PID: {os.getpid()}, el PID de mi padre es: {os.getppid()}")
    time.sleep(10)  # Esperar 5 segundos antes de terminar
    print(a)
else:
    print("Error al crear el proceso hijo")

