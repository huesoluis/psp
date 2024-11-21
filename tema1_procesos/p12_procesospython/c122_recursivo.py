import os

def show_parent_processes(pid):
    print(f"Iniciando desde el proceso actual con PID {pid}:\n")
    while pid != 0:
        print(f"Proceso actual: PID = {pid}")
        stat_file_path = f"/proc/{pid}/stat"
        print(f"Leyendo información desde {stat_file_path}...")
        if not os.path.exists(stat_file_path):
            print(f"Error: No se encontró el archivo {stat_file_path}. El proceso puede haber terminado.")
            break
        
        # Leer el archivo de estadísticas del proceso
        with open(stat_file_path, "r") as file:
            data = file.read().split()
            ppid = int(data[3])  # El cuarto campo corresponde al PPID
            print(f"Padre del proceso actual: PPID = {ppid}\n")
        
        # Asignar el PPID como el nuevo PID para seguir subiendo en la jerarquía
        pid = ppid

    print("Se alcanzó el proceso raíz o no se pudo continuar.\n")

def main():
    # Obtener el PID del proceso actual
    current_pid = os.getpid()
    print("### Inicio del programa para mostrar la cadena de procesos padres ###\n")
    print(f"El PID del programa actual es {current_pid}.")
    print("Ahora se mostrará la jerarquía completa de procesos padres:\n")
    show_parent_processes(current_pid)

if __name__ == "__main__":
    main()

