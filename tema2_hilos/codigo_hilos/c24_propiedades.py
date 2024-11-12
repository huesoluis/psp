#codigo c24_propiedades.py
import threading
import random

# Función que cada hilo ejecutará
def calcular_suma(segmento, indice):
    suma = sum(segmento)
    hilo_actual = threading.current_thread()
    print(f'Hilo {indice} con nombre "{hilo_actual.name}" ejecutándose. Calculando la suma de su segmento.')
    print(f'Hilo {indice}: Identificador = {hilo_actual.ident}, Daemon = {hilo_actual.daemon}')
    print(f'Hilo {indice}: Suma del segmento = {suma}\n')

# Generar un arreglo de números aleatorios
tamaño_arreglo = 100
arreglo = [random.randint(1, 10) for _ in range(tamaño_arreglo)]

# Dividir el arreglo en segmentos para cada hilo
numero_hilos = 5
segmentos = [arreglo[i::numero_hilos] for i in range(numero_hilos)]

hilos = []

for i in range(numero_hilos):
    hilo = threading.Thread(target=calcular_suma, args=(segmentos[i], i), name=f'HiloCalculador-{i}')
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print('Cálculo completado.')
