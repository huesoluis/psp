import os

def print_pid_and_parents():
    current_pid = os.getpid()  # Obtener el PID del proceso actual
    parent_pid = os.getppid()  # Obtener el PID del proceso padre
    
    print(f"Proceso actual (PID): {current_pid}")
    
    # Repetir hasta llegar al proceso raíz (PID 1)
    while parent_pid != 1:
        print(f"Padre del proceso (PID): {parent_pid}")
        current_pid = parent_pid
        parent_pid = os.getppid()  # Actualizar el PID del padre
        
    # Imprimir el proceso raíz
    print(f"Proceso raíz (PID): {parent_pid}")

if __name__ == "__main__":
    print_pid_and_parents()

