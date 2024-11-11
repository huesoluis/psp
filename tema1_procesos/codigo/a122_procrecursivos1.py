import psutil

def print_recursive_parents():
    current_process = psutil.Process()  # Obtener el proceso actual
    parent_chain = []

    # Mientras haya un padre, agregarlo a la cadena de procesos
    while current_process:
        parent_pid = current_process.ppid()  # Obtener el PID del padre
        parent_chain.append((current_process.pid, parent_pid))
        if parent_pid == 0:  # Si el padre es 0, se ha llegado al final
            break
        try:
            current_process = psutil.Process(parent_pid)  # Mover al proceso padre
        except psutil.NoSuchProcess:
            break  # Si el proceso padre no existe, salir del bucle

    # Imprimir la cadena de procesos
    for pid, ppid in parent_chain:
        print(f"PID: {pid}, Parent PID: {ppid}")

# Ejecutar la función
print_recursive_parents()

