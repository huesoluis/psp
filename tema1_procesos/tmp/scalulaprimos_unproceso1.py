import time

def es_primo(n):
    """Función que determina si un número es primo."""
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def contar_primos(lista_numeros):
    """Cuenta la cantidad de números primos en una lista."""
    return sum(1 for num in lista_numeros if es_primo(num))

def leer_lista(filename):
    """Lee una lista de números enteros desde un archivo, separados por comas.
    Ignora valores no válidos que no puedan convertirse a enteros.
    """
    with open(filename, 'r') as f:
        contenido = f.read().strip()
    
    # Separar los números por coma, eliminando espacios, y convertir a enteros si es posible
    lista_numeros = []
    for item in contenido.split(','):
        item = item.strip()  # Eliminar espacios en blanco
        try:
            numero = int(item)  # Intentar convertir a entero
            lista_numeros.append(numero)
        except ValueError:
            # Si no se puede convertir a entero, ignorar este valor
            print(f"Advertencia: '{item}' no es un número válido y se ha omitido.")
    return lista_numeros

def ejecutar_programa():
    # Medir el tiempo total del script
    tiempo_inicial = time.time()

    # Leer los números del archivo
    lista_numeros = leer_lista("short_lista")

    # Medir el tiempo de proceso de cálculo de primos
    tiempo_proceso_inicial = time.time()
    numero_primos = contar_primos(lista_numeros)
    tiempo_proceso_final = time.time()

    # Tiempo total del script
    tiempo_total_final = time.time()

    # Calcular tiempos
    tiempo_proceso = tiempo_proceso_final - tiempo_proceso_inicial
    tiempo_total = tiempo_total_final - tiempo_inicial

    return numero_primos, tiempo_proceso, tiempo_total

if __name__ == "__main__":
    total_primos = 0
    suma_tiempos_proceso = 0
    suma_tiempos_totales = 0
    num_ejecuciones = 10

    # Ejecutar el programa 10 veces
    for i in range(num_ejecuciones):
        print(f"--- Ejecución número {i + 1} ---")
        numero_primos, tiempo_proceso, tiempo_total = ejecutar_programa()
        total_primos = numero_primos  # Se asume que el número de primos es el mismo en cada ejecución
        suma_tiempos_proceso += tiempo_proceso
        suma_tiempos_totales += tiempo_total
        print(f"Número de primos: {numero_primos}")
        print(f"Tiempo del proceso de cálculo de primos: {tiempo_proceso:.6f} segundos")
        print(f"Tiempo total del script: {tiempo_total:.6f} segundos\n")

    # Calcular y mostrar los promedios
    promedio_tiempo_proceso = suma_tiempos_proceso / num_ejecuciones
    promedio_tiempo_total = suma_tiempos_totales / num_ejecuciones

    print(f"--- Resultados finales después de {num_ejecuciones} ejecuciones ---")
    print(f"Promedio de tiempo de proceso de cálculo de primos: {promedio_tiempo_proceso:.6f} segundos")
    print(f"Promedio de tiempo total del script: {promedio_tiempo_total:.6f} segundos")
    print(f"Número total de primos: {total_primos}")
