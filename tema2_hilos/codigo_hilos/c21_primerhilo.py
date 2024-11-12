#código c21_primerhilo.py
import threading
import time

def worker():
    print("Hilo iniciado")
    time.sleep(10)
    print("Hilo terminado")

# Hilo nuevo
hilo = threading.Thread(target=worker)

# Inicia el hilo (estado: Running)
hilo.start()

# Espera la terminación del hilo (estado: Waiting)
hilo.join()

print("Finalización del programa")
