import os
import time
import threading

def calcular_tamano(directorios, resultados, indice):
    """Función para calcular el tamaño total de una lista de directorios."""
    tamanio_total = 0
    for directorio in directorios:
        for ruta, _, archivos in os.walk(directorio):
            for archivo in archivos:
                archivo_path = os.path.join(ruta, archivo)
                try:
                    tamanio_total += os.path.getsize(archivo_path)
                except FileNotFoundError:
                    continue
    resultados[indice] = tamanio_total

if __name__ == "__main__":
    directorios = ["/usr", "/var", "/home"]
    mitad = len(directorios) // 2
    resultados = [0, 0]
    
    print("\n--- Con dos hilos ---")
    inicio = time.time()
    hilo1 = threading.Thread(target=calcular_tamano, args=(directorios[:mitad], resultados, 0))
    hilo2 = threading.Thread(target=calcular_tamano, args=(directorios[mitad:], resultados, 1))
    hilo1.start()
    hilo2.start()
    hilo1.join()
    hilo2.join()
    tamanio = sum(resultados)
    tiempo = time.time() - inicio
    print(f"Tamaño total: {tamanio / (1024 ** 3):.2f} GB")
    print(f"Tiempo: {tiempo:.2f} segundos")

