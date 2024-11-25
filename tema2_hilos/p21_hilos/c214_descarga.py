import threading
import requests
import time

# URL de la ISO de TinyCore Linux
url = "http://tinycorelinux.net/15.x/x86/release/Core-current.iso"
archivo_destino = "Core-current.iso"

# Variables globales para el progreso de descarga
tamanio_descargado = 0
tamanio_total = 0

# Función para descargar el archivo
def descargar_archivo():
    global tamanio_descargado

    # Realizar una petición HTTP GET para descargar el archivo
    respuesta = requests.get(url, stream=True)

    # Descargar el archivo por bloques y escribirlo en disco
    with open(archivo_destino, "wb") as archivo:
        for data in respuesta.iter_content(chunk_size=1024):
            archivo.write(data)
            tamanio_descargado += len(data)  # Actualizar el tamaño descargado

# Función para mostrar el progreso de descarga
def mostrar_progreso():
    global tamanio_descargado, tamanio_total
    while tamanio_descargado < tamanio_total:
        porcentaje = (tamanio_descargado / tamanio_total) * 100
        print(f"Descargado: {porcentaje:.2f}%")
        time.sleep(1)
    print("Descarga completada al 100%")

def main():
    global tamanio_total

    # Obtener el tamaño total del archivo antes de iniciar los hilos
    respuesta = requests.head(url)
    tamanio_total = int(respuesta.headers.get('content-length', 0))
    print(f"Tamaño total del archivo: {tamanio_total / (1024 ** 2):.2f} MB")

    # Crear hilo para descargar el archivo
    hilo_descarga = threading.Thread(target=descargar_archivo)
    
    # Crear hilo para mostrar el progreso
    hilo_progreso = threading.Thread(target=mostrar_progreso)

    # Iniciar ambos hilos
    hilo_descarga.start()
    hilo_progreso.start()

    # Esperar a que los hilos terminen
    hilo_descarga.join()
    hilo_progreso.join()

if __name__ == "__main__":
    main()

