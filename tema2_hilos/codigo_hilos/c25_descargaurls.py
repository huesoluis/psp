#código c25_descarga.py
import threading
import time
import requests

def descargar_contenido(url):
    print(f"Iniciando descarga de: {url}")
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(f"Descarga completada de: {url}")
        else:
            print(f"Error al descargar {url}: Código de estado {respuesta.status_code}")
    except requests.RequestException as e:
        print(f"Error al descargar {url}: {e}")

# Lista de URLs a descargar
urls = [
    'https://www.example.com',
    'https://www.python.org',
    'https://www.github.com',
    # Agrega más URLs según sea necesario
]

# Crear y almacenar los hilos
hilos = []
for url in urls:
    hilo = threading.Thread(target=descargar_contenido, args=(url,))
    hilos.append(hilo)
    hilo.start()

# Monitorear el estado de los hilos
while any(hilo.is_alive() for hilo in hilos):
    print("Esperando que las descargas finalicen...")
    time.sleep(2)

print("Todas las descargas han finalizado.")
