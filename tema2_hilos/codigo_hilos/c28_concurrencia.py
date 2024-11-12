import threading
import time

contador = 0

def incrementar():
    global contador
    for _ in range(200000):
        time.sleep(0.0001)  # Introduce un retraso pequeño
        contador += 1

def decrementar():
    global contador
    for _ in range(200000):
        time.sleep(0.001)  # Introduce un retraso pequeño
        contador -= 1

hilo1 = threading.Thread(target=incrementar)
hilo2 = threading.Thread(target=decrementar)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f'Valor final del contador: {contador}')

