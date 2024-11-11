import subprocess

def list_active_processes_with_ps():
    """
    Función que ejecuta el comando 'ps aux' para listar los procesos activos.
    """
    # Ejecutamos el comando `ps aux` usando subprocess
    result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, text=True)
    
    # Mostramos la salida del comando
    print(result.stdout)

def main():
    """
    Función principal del programa.
    """
    print("Listando los procesos activos usando 'ps aux':")
    list_active_processes_with_ps()

# Punto de entrada principal del programa
if __name__ == "__main__":
    main()

