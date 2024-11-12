import threading
import requests

def obtener_tamano(url):
    """
    Obtiene el tamaño del archivo desde la URL usando una solicitud HEAD.
    """
    respuesta = requests.head(url)
    if respuesta.status_code == 200 and 'Content-Length' in respuesta.headers:
        return int(respuesta.headers['Content-Length'])
    else:
        raise Exception("No se pudo obtener el tamaño del archivo o el servidor no admite esta operación.")

def descargar_parte(url, inicio, fin, nombre_archivo):
    """
    Descarga una parte del archivo desde 'inicio' hasta 'fin' y lo guarda en 'nombre_archivo'.
    """
    headers = {'Range': f'bytes={inicio}-{fin}'}
    respuesta = requests.get(url, headers=headers, stream=True)
    if respuesta.status_code in (200, 206):  # 206 significa "Partial Content"
        with open(nombre_archivo, 'wb') as archivo:
            for chunk in respuesta.iter_content(chunk_size=8192):
                archivo.write(chunk)
    else:
        raise Exception(f"Error al descargar la parte {inicio}-{fin} del archivo.")

def fusionar_archivos(nombre_archivo1, nombre_archivo2, nombre_final):
    """
    Fusiona dos archivos en uno solo.
    """
    with open(nombre_final, 'wb') as archivo_final:
        for nombre_parte in [nombre_archivo1, nombre_archivo2]:
            with open(nombre_parte, 'rb') as archivo_parte:
                archivo_final.write(archivo_parte.read())

def main():
    # URL del archivo a descargar
    url = 'https://distro.ibiblio.org/tinycorelinux/15.x/x86/release/Core-15.0.iso'

    # Obtener el tamaño total del archivo
    tamano_total = obtener_tamano(url)
    mitad = tamano_total // 2

    # Definir los rangos de descarga para cada hilo
    inicio1, fin1 = 0, mitad - 1
    inicio2, fin2 = mitad, tamano_total - 1

    # Nombres de archivos temporales para cada parte descargada
    nombre_archivo1 = 'parte1.tmp'
    nombre_archivo2 = 'parte2.tmp'
    nombre_archivo_final = 'archivo_descargado.zip'

    # Crear hilos para descargar cada parte
    hilo1 = threading.Thread(target=descargar_parte, args=(url, inicio1, fin1, nombre_archivo1))
    hilo2 = threading.Thread(target=descargar_parte, args=(url, inicio2, fin2, nombre_archivo2))

    # Iniciar los hilos
    hilo1.start()
    hilo2.start()

    # Esperar a que ambos hilos terminen
    hilo1.join()
    hilo2.join()

    # Fusionar ambas partes en un archivo final
    fusionar_archivos(nombre_archivo1, nombre_archivo2, nombre_archivo_final)

    print(f"Descarga completada. Archivo guardado como {nombre_archivo_final}")

if __name__ == "__main__":
    main()

