import os
import time

def calcular_tamano(directorios):
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
    return tamanio_total

if __name__ == "__main__":
    directorios = ["/usr", "/var", "/home"]
    
    print("\n--- Modo normal (sin hilos) ---")
    inicio = time.time()
    tamanio = calcular_tamano(directorios)
    tiempo = time.time() - inicio
    print(f"Tamaño total: {tamanio / (1024 ** 3):.2f} GB")
    print(f"Tiempo: {tiempo:.2f} segundos")

