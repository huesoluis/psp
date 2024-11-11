import os
import time

# Variable global que será modificada por el padre y el hijo
variable_global = 0

# Crear un proceso hijo usando fork
pid = os.fork()

if pid > 0:
    # Este bloque es ejecutado por el proceso padre
    print(f"Padre (PID: {os.getpid()}), valor inicial de variable_global: {variable_global}")
    
    # Modificar la variable global en el proceso padre
    variable_global += 10
    print(f"Padre (PID: {os.getpid()}), variable_global después de modificación: {variable_global}")
    
    # Esperar unos segundos para asegurarnos de que el hijo también imprima
    time.sleep(2)
    print(f"Padre (PID: {os.getpid()}), valor final de variable_global: {variable_global}")

elif pid == 0:
    # Este bloque es ejecutado por el proceso hijo
    print(f"Hijo (PID: {os.getpid()}), valor inicial de variable_global: {variable_global}")
    
    # Modificar la variable global en el proceso hijo
    variable_global += 20
    print(f"Hijo (PID: {os.getpid()}), variable_global después de modificación: {variable_global}")
    
    # Esperar unos segundos para asegurarse de que el padre también imprima
    time.sleep(2)
    print(f"Hijo (PID: {os.getpid()}), valor final de variable_global: {variable_global}")
else:
    print("Error al crear el proceso hijo")

