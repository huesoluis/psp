"""
Medición del tiempo total:

Usa time.time() para obtener el tiempo en segundos antes y después de la función contar_primos_en_fichero.
La diferencia (fin_tiempo - inicio_tiempo) da el tiempo total en segundos que tardó en contar los números primos.
Salida:

Imprime el total de números primos en el archivo.
Muestra el tiempo total transcurrido en segundos, con cuatro decimales de precisión.
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
    
    # Medir el tiempo inicial
    inicio_tiempo = time.time()
    
    # Calcular el número total de primos
    total_primos = contar_primos_en_fichero(fichero)
    
    # Medir el tiempo final
    fin_tiempo = time.time()
    
    # Calcular el tiempo total
    tiempo_total = fin_tiempo - inicio_tiempo
    
    # Mostrar los resultados
    print(f"Total de números primos en el archivo '{fichero}': {total_primos}")
    print(f"Tiempo total de cálculo: {tiempo_total:.4f} segundos")

