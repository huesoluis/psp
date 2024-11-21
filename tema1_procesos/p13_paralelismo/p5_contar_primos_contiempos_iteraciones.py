"""
Variables para almacenar los tiempos:

tiempos_totales y tiempos_proceso son listas donde se almacenan los tiempos totales y los tiempos de CPU para cada una de las 10 iteraciones.
Bucle de 10 iteraciones:

En cada iteración, se mide el tiempo total (time.time()) y el tiempo de proceso de CPU (time.process_time()).
Luego de ejecutar la función contar_primos_en_fichero, se calcula el tiempo transcurrido para esa iteración y se almacena en las listas.
Cálculo de tiempos promedio:

Luego del bucle, se calcula el promedio de los tiempos totales y el promedio de los tiempos de CPU dividiendo la suma de cada lista entre el número de iteraciones (iteraciones).
Resultado:

Se muestra el total de números primos en el archivo y los tiempos promedio de cálculo en tiempo de reloj y de CPU.
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
    
    # Número de iteraciones
    iteraciones = 10
    tiempos_totales = []
    tiempos_proceso = []
    
    for it in range(iteraciones):
        print(f"Inicio iteración '{it}'")
        # Medir el tiempo total y el tiempo de proceso de CPU
        inicio_tiempo_total = time.time()
        inicio_tiempo_proceso = time.process_time()
        
        # Calcular el número total de primos
        total_primos = contar_primos_en_fichero(fichero)
        
        # Medir el tiempo final total y de proceso de CPU
        fin_tiempo_total = time.time()
        fin_tiempo_proceso = time.process_time()
        
        # Calcular los tiempos para esta iteración
        tiempo_total = fin_tiempo_total - inicio_tiempo_total
        tiempo_proceso = fin_tiempo_proceso - inicio_tiempo_proceso
        
        # Almacenar los tiempos
        tiempos_totales.append(tiempo_total)
        tiempos_proceso.append(tiempo_proceso)
    
    # Calcular la media de los tiempos
    tiempo_total_promedio = sum(tiempos_totales) / iteraciones
    tiempo_proceso_promedio = sum(tiempos_proceso) / iteraciones
    
    # Mostrar los resultados
    print(f"Total de números primos en el archivo '{fichero}': {total_primos}")
    print(f"Tiempo total promedio de cálculo (reloj): {tiempo_total_promedio:.4f} segundos")
    print(f"Tiempo de CPU promedio de proceso: {tiempo_proceso_promedio:.4f} segundos")

