import time
import psutil

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_primos(numeros):
    return sum(1 for numero in numeros if es_primo(numero))

def calcular_primos(fichero, iteraciones=10):
    tiempos_totales = []
    tiempos_cpu = []

    # Leer los números del fichero
    with open(fichero, 'r') as f:
        numeros = [int(line.strip()) for line in f]

    # Realizar el cálculo 10 veces
    for _ in range(iteraciones):
        start_time = time.time()
        start_cpu = psutil.cpu_times()

        contar_primos(numeros)

        end_time = time.time()
        end_cpu = psutil.cpu_times()

        tiempos_totales.append(end_time - start_time)
        tiempos_cpu.append(end_cpu - start_cpu)

    tiempo_medio = sum(tiempos_totales) / iteraciones
    tiempo_medio_cpu = sum(tiempos_cpu) / iteraciones

    print(f"Tiempo total promedio: {tiempo_medio:.4f} segundos")
    print(f"Tiempo de CPU promedio: {tiempo_medio_cpu:.4f} segundos")

if __name__ == "__main__":
    calcular_primos("short_lista")

