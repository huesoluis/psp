import time
import multiprocessing
import csv

# Función para generar ocho listas a partir de un archivo de números
def generar_listas(fichero):
    """
    Lee un archivo de números y divide la lista en ocho partes iguales.

    Parámetros:
    fichero (str): Ruta del archivo de texto con una lista de números enteros.

    Retorna:
    list: Ocho listas de números enteros.
    """
    with open(fichero, 'r') as f:
        numeros = list(map(int, f.readlines()))
    octavo = len(numeros) // 8
    listas = [numeros[i*octavo:(i+1)*octavo] for i in range(8)]
    return listas

# Función para contar primos en una lista de números y guardar el resultado en la cola
def contar_primos(numeros, queue):
    """
    Cuenta la cantidad de números primos en una lista de números y coloca el resultado en la cola.

    Parámetros:
    numeros (list): Lista de números enteros.
    queue (multiprocessing.Queue): Cola para almacenar el resultado del proceso.
    """
    cuenta_primos = sum(1 for n in numeros if es_primo(n))
    queue.put(cuenta_primos)  # Envía el resultado a la cola

# Función auxiliar que verifica si un número es primo
def es_primo(n):
    """
    Determina si un número es primo.

    Parámetros:
    n (int): Número entero a verificar.

    Retorna:
    bool: True si el número es primo, False en caso contrario.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función para guardar el número de procesos y el tiempo total en un archivo CSV
def guardar_resultado_csv(num_procesos, tiempo_total, total_primos, nombre_archivo="resultados.csv"):
    """
    Guarda el número de procesos, el tiempo total y el número total de primos en un archivo CSV.

    Parámetros:
    num_procesos (int): Número de procesos utilizados.
    tiempo_total (float): Tiempo total dedicado en segundos.
    total_primos (int): Número total de primos encontrados.
    nombre_archivo (str): Nombre del archivo CSV donde se guardarán los resultados.
    """
    with open(nombre_archivo, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([num_procesos, tiempo_total, total_primos])

# Función principal que organiza la ejecución en paralelo y mide el tiempo de CPU
def main():
    fichero = "long_list"  # Especifica la ruta de tu fichero aquí
    num_procesos = 8  # Número de procesos utilizados

    # Genera las ocho listas dividiendo el archivo en ocho partes
    listas = generar_listas(fichero)

    # Crea una cola para almacenar los resultados de cada proceso
    queue = multiprocessing.Queue()

    # Crea los procesos para cada lista
    procesos = [
        multiprocessing.Process(target=contar_primos, args=(listas[i], queue))
        for i in range(num_procesos)
    ]

    # Inicia el cronómetro de CPU
    start_cpu = time.time()

    # Inicia los ocho procesos
    for proceso in procesos:
        proceso.start()

    # Espera a que los ocho procesos terminen
    for proceso in procesos:
        proceso.join()

    # Finaliza el cronómetro de CPU y registra el tiempo
    end_cpu = time.time()
    tiempo_total = end_cpu - start_cpu

    # Recupera y suma los resultados de la cola
    total_primos = sum(queue.get() for _ in range(num_procesos))

    print(f"Tiempo total CPU con {num_procesos} procesos: {tiempo_total:.4f} segundos")
    print(f"Total de números primos encontrados: {total_primos}")

    # Guarda el resultado en un archivo CSV
    guardar_resultado_csv(num_procesos, tiempo_total, total_primos)

# Llamada al main
if __name__ == "__main__":
    main()

