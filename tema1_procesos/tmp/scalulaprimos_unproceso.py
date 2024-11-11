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
    """Lee una lista de números enteros desde un archivo, separados por comas."""
    with open(filename, 'r') as f:
        contenido = f.read().strip()
    lista_numeros = list(map(int, contenido.split(',')))
    return lista_numeros

if __name__ == "__main__":
    # Medir el tiempo total del script
    tiempo_inicial = time.time()
    
    # Leer los números del archivo
    lista_numeros = leer_lista("short_lista")
    
    # Medir el tiempo de proceso de cálculo de primos
    tiempo_proceso_inicial = time.process_time()
    numero_primos = contar_primos(lista_numeros)
    tiempo_proceso_final = time.process_time()
    
    # Tiempo total del script
    tiempo_total_final = time.time()
    
    # Mostrar resultados
    print(f"Número total de primos: {numero_primos}")
    print(f"Tiempo del proceso de cálculo de primos: {tiempo_proceso_final - tiempo_proceso_inicial:.6f} segundos")
    print(f"Tiempo total del script: {tiempo_total_final - tiempo_inicial:.6f} segundos")

