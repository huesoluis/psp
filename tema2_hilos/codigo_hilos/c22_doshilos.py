#codigo c22_doshilos.py
import threading
import time

def tarea(nombre_hilo):
    for i in range(5):  # 5 iteraciones * 2 segundos = 10 segundos
        print(f"{nombre_hilo} está en ejecución. Iteración {i + 1}")
        time.sleep(2)
    print(f"{nombre_hilo} ha finalizado.")

# Crear los hilos
hilo1 = threading.Thread(target=tarea, args=("Hilo-1",))
hilo2 = threading.Thread(target=tarea, args=("Hilo-2",))

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Ambos hilos han finalizado.")
