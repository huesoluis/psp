import threading
import time
import random

# Variable compartida
contador = 0

# Número de iteraciones por hilo
ITERACIONES = 100

# Función que incrementa el contador sin bloqueo
def incrementar(nombre_hilo):
    global contador
    for _ in range(ITERACIONES):
        # Mostrar qué hilo está en ejecución
        print(f"Hilo {nombre_hilo} accediendo a contador: {contador}")
        
        # Simular una condición de carrera con retardo
        valor_temporal = contador
        time.sleep(random.uniform(0.0001, 0.001))  # Retardo intencional
        contador = valor_temporal + 1

# Crear hilos
hilo1 = threading.Thread(target=incrementar, args=("Hilo-1",))
hilo2 = threading.Thread(target=incrementar, args=("Hilo-2",))

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar a que terminen los hilos
hilo1.join()
hilo2.join()

# Mostrar el valor final del contador
print(f"Valor esperado del contador: {2 * ITERACIONES}")
print(f"Valor real del contador: {contador}")

