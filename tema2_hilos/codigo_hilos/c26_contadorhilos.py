#c26_contadorhilos.py
import threading
import time

contador = 0

def incrementar():
    print("iniciando hilo inc")
    global contador
    for _ in range(1000):
        print(f"iteracion inc contador: {contador}")
        time.sleep(0.1)
        contador += 1

def decrementar():
    print("iniciando hilo dec")
    global contador
    print("iniciando hilo dec desp contador")
    for _ in range(1000):
        time.sleep(0.1)
        print(f"iteracion dec contador: {contador}")
        contador -= 1
        print(f"{contador}")

hilo1 = threading.Thread(target=incrementar)
hilo2 = threading.Thread(target=decrementar)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f'Valor final del contador: {contador}')
