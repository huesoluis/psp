import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import psutil
import time

# Variables globales para almacenar datos
cpu_data = []
mem_data = []
disk_data = []
time_data = []

# Función para actualizar datos del uso de CPU
def monitor_cpu():
    global cpu_data, time_data
    while True:
        cpu_data.append(psutil.cpu_percent(interval=0.1))
        time_data.append(time.time())
        if len(cpu_data) > 100:
            cpu_data.pop(0)
            time_data.pop(0)

# Función para actualizar datos del uso de memoria
def monitor_memory():
    global mem_data
    while True:
        mem_data.append(psutil.virtual_memory().percent)
        if len(mem_data) > 100:
            mem_data.pop(0)
        time.sleep(0.1)

# Función para actualizar datos del uso de disco
def monitor_disk():
    global disk_data
    while True:
        disk_data.append(psutil.disk_usage('/').percent)
        if len(disk_data) > 100:
            disk_data.pop(0)
        time.sleep(0.1)

# Función para graficar el uso de CPU
def plot_cpu(ax):
    def update(frame):
        ax.clear()
        ax.plot(time_data[-100:], cpu_data[-100:], label='CPU Usage (%)')
        ax.set_title("CPU Usage")
        ax.set_xlabel("Time")
        ax.set_ylabel("Percentage")
        ax.legend()
        ax.grid(True)
    return update

# Función para graficar el uso de memoria
def plot_memory(ax):
    def update(frame):
        ax.clear()
        ax.plot(mem_data[-100:], label='Memory Usage (%)')
        ax.set_title("Memory Usage")
        ax.set_xlabel("Time")
        ax.set_ylabel("Percentage")
        ax.legend()
        ax.grid(True)
    return update

# Función para graficar el uso de disco
def plot_disk(ax):
    def update(frame):
        ax.clear()
        ax.plot(disk_data[-100:], label='Disk Usage (%)')
        ax.set_title("Disk Usage")
        ax.set_xlabel("Time")
        ax.set_ylabel("Percentage")
        ax.legend()
        ax.grid(True)
    return update

def main():
    # Crear hilos para monitorear CPU, memoria y disco
    threading.Thread(target=monitor_cpu, daemon=True).start()
    threading.Thread(target=monitor_memory, daemon=True).start()
    threading.Thread(target=monitor_disk, daemon=True).start()

    # Configurar gráficos
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))

    # Animaciones
    ani_cpu = FuncAnimation(fig, plot_cpu(axs[0]), interval=100)
    ani_memory = FuncAnimation(fig, plot_memory(axs[1]), interval=100)
    ani_disk = FuncAnimation(fig, plot_disk(axs[2]), interval=100)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

