import threading
import time
import random

# Variable compartida
contador = 0

# Número de iteraciones por hilo
ITERACIONES = 100

# Crear un bloqueo
bloqueo = threading.Lock()

# Función que incrementa el contador con bloqueo
def incrementar_con_bloqueo(nombre_hilo):
    global contador
    for _ in range(ITERACIONES):
        with bloqueo:  # Adquirir el bloqueo
            print(f"Hilo {nombre_hilo} accediendo a contador: {contador}")
            valor_temporal = contador
            time.sleep(random.uniform(0.0001, 0.001))  # Retardo intencional
            contador = valor_temporal + 1

# Crear hilos
hilo1 = threading.Thread(target=incrementar_con_bloqueo, args=("Hilo-1",))
hilo2 = threading.Thread(target=incrementar_con_bloqueo, args=("Hilo-2",))

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar a que terminen los hilos
hilo1.join()
hilo2.join()

# Mostrar el valor final del contador
print(f"Valor esperado del contador: {2 * ITERACIONES}")
print(f"Valor real del contador: {contador}")

