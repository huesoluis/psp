import time
import csv

# Función para generar una lista completa a partir de un archivo de números
def generar_lista(fichero):
    """
    Lee un archivo de números y retorna la lista completa de números enteros.

    Parámetros:
    fichero (str): Ruta del archivo de texto con una lista de números enteros.

    Retorna:
    list: Lista completa de números enteros.
    """
    with open(fichero, 'r') as f:
        numeros = list(map(int, f.readlines()))
    return numeros

# Función para contar primos en una lista de números
def contar_primos(numeros):
    """
    Cuenta la cantidad de números primos en una lista de números.

    Parámetros:
    numeros (list): Lista de números enteros.

    Retorna:
    int: Número de primos en la lista.
    """
    return sum(1 for n in numeros if es_primo(n))

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

# Función principal que organiza la ejecución y mide el tiempo de CPU
def main():
    fichero = "long_list"  # Especifica la ruta de tu fichero aquí
    num_procesos = 1  # Número de procesos utilizados

    # Genera la lista completa de números
    lista = generar_lista(fichero)

    # Inicia el cronómetro de CPU
    #start_cpu = time.process_time()
    start_cpu = time.time()

    # Cuenta el total de números primos en la lista completa
    total_primos = contar_primos(lista)

    # Finaliza el cronómetro de CPU y registra el tiempo
    # end_cpu = time.process_time()
    end_cpu = time.time()
    tiempo_total = end_cpu - start_cpu

    print(f"Tiempo total CPU con {num_procesos} proceso: {tiempo_total:.4f} segundos")
    print(f"Total de números primos encontrados: {total_primos}")

    # Guarda el resultado en un archivo CSV
    guardar_resultado_csv(num_procesos, tiempo_total, total_primos)

# Llamada al main
if __name__ == "__main__":
    main()

