import psutil
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time

# Función para obtener el uso de memoria y CPU
def obtener_datos_sistema():
    memoria = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)
    return memoria.percent, cpu

# Variables para almacenar datos
memoria_usada = []
cpu_usada = []
tiempo = []

# Tiempo total para monitorear (en segundos)
tiempo_total = 20
intervalo = 1  # Intervalo entre cada medición (segundos)

# Monitorear y graficar
for i in range(1, tiempo_total + 1):
    mem, cpu = obtener_datos_sistema()
    memoria_usada.append(mem)
    cpu_usada.append(cpu)
    tiempo.append(i * intervalo)
    
    # Limpiar la salida anterior
    clear_output(wait=True)
    
    # Crear el gráfico
    plt.figure(figsize=(10, 5))
    
    # Gráfico de uso de memoria
    plt.subplot(1, 2, 1)
    plt.plot(tiempo, memoria_usada, label='Uso de Memoria (%)', color='blue')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Memoria (%)')
    plt.title('Monitoreo de Memoria')
    plt.ylim(0, 100)
    plt.grid(True)
    plt.legend()
    
    # Gráfico de uso de CPU
    plt.subplot(1, 2, 2)
    plt.plot(tiempo, cpu_usada, label='Uso de CPU (%)', color='green')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('CPU (%)')
    plt.title('Monitoreo de CPU')
    plt.ylim(0, 100)
    plt.grid(True)
    plt.legend()
    
    # Mostrar el gráfico actualizado
    plt.tight_layout()
    plt.show()
    
    # Pausa antes de la siguiente actualización
    time.sleep(intervalo)

