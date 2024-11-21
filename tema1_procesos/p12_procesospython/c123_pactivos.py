import psutil

def list_active_processes():
    print(f"{'PID':<10}{'Nombre':<25}{'Usuario':<15}{'% CPU':<10}{'% Memoria':<10}")
    print("-" * 70)
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            user = proc.info['username']
            cpu = proc.info['cpu_percent']
            memory = proc.info['memory_percent']
            print(f"{pid:<10}{name:<25}{user:<15}{cpu:<10.1f}{memory:<10.1f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

if __name__ == "__main__":
    print("Procesos activos en el sistema usando psutil:\n")
    list_active_processes()

