import threading
import time
import random

# Variable compartida
contador = 0

# Número de iteraciones por hilo
ITERACIONES = 1000

# Función que incrementa el contador con un retardo
def incrementar():
    global contador
    for _ in range(ITERACIONES):
        # Simular un retardo aleatorio
        valor_temporal = contador
        time.sleep(random.uniform(0.0001, 0.001))  # Retardo intencional
        contador = valor_temporal + 1

# Crear hilos
hilo1 = threading.Thread(target=incrementar)
hilo2 = threading.Thread(target=incrementar)

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar a que terminen los hilos
hilo1.join()
hilo2.join()

# Mostrar el valor final del contador
print(f"Valor esperado del contador: {2 * ITERACIONES}")
print(f"Valor real del contador: {contador}")

