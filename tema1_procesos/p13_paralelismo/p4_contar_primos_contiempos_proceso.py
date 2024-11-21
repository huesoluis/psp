"""
Medición del tiempo total:

Usamos time.time() para medir el tiempo total (reloj) desde el inicio hasta el final del cálculo.
Medición del tiempo de proceso de CPU:

Usamos time.process_time(), que mide solo el tiempo de CPU que el proceso ha utilizado directamente.
Esto excluye cualquier tiempo en el que el proceso estuvo en espera o compartiendo recursos con otros procesos.
Resultados:

Tiempo total de cálculo: Es el tiempo transcurrido de reloj, incluyendo cualquier pausa o interferencia de otros procesos.
Tiempo de CPU de proceso: Mide el tiempo dedicado exclusivamente a la ejecución del proceso en la CPU.
"""

import time

def es_primo(numero):
    """Función que determina si un número es primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_primos_en_fichero(fichero):
    """Función que lee un archivo y cuenta la cantidad de números primos."""
    total_primos = 0
    
    # Leer los números del fichero
    with open(fichero, 'r') as f:
        for linea in f:
            try:
                numero = int(linea.strip())
                if es_primo(numero):
                    total_primos += 1
            except ValueError:
                print(f"Valor no válido encontrado: {linea.strip()} (omitido)")
    
    return total_primos

if __name__ == "__main__":
    # Nombre del fichero que contiene los números
    fichero = "long_list"
    
    # Medir el tiempo total y el tiempo de proceso de CPU
    inicio_tiempo_total = time.time()
    inicio_tiempo_proceso = time.process_time()
    
    # Calcular el número total de primos
    total_primos = contar_primos_en_fichero(fichero)
    
    # Medir el tiempo final total y de proceso de CPU
    fin_tiempo_total = time.time()
    fin_tiempo_proceso = time.process_time()
    
    # Calcular los tiempos
    tiempo_total = fin_tiempo_total - inicio_tiempo_total
    tiempo_proceso = fin_tiempo_proceso - inicio_tiempo_proceso
    
    # Mostrar los resultados
    print(f"Total de números primos en el archivo '{fichero}': {total_primos}")
    print(f"Tiempo total de cálculo (reloj): {tiempo_total:.4f} segundos")
    print(f"Tiempo de CPU de proceso: {tiempo_proceso:.4f} segundos")

