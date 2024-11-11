import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Inicialización de listas para almacenar los datos de la memoria
tiempos = []
memoria_usada = []

# Función para obtener el uso de la memoria
def actualizar_datos(i):
    # Obtener los datos de la memoria
    memoria = psutil.virtual_memory()
    
    # Agregar los datos de memoria utilizada en porcentaje a la lista
    tiempos.append(i)
    memoria_usada.append(memoria.percent)
    print(memoria)
    # Limitar la cantidad de datos mostrados a los últimos 50
    tiempos_limited = tiempos[-50:]
    memoria_limited = memoria_usada[-50:]

    # Limpiar el gráfico anterior y graficar los nuevos datos
    plt.cla()
    plt.plot(tiempos_limited, memoria_limited, label='Memoria usada (%)')
    
    # Formato del gráfico
    plt.ylim([0, 100])  # Límite del porcentaje de memoria
    plt.xlabel("Tiempo (segundos)")
    plt.ylabel("Uso de memoria (%)")
    plt.title("Monitoreo Dinámico del Uso de Memoria")
    plt.grid(True)
    plt.legend(loc='upper left')

# Configuración del gráfico
fig = plt.figure(figsize=(10, 5))

# Animación del gráfico, llamando a la función cada 1000ms (1 segundo)
ani = FuncAnimation(plt.gcf(), actualizar_datos, interval=1000)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

