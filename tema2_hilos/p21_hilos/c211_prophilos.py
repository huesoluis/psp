import threading
import time

def mostrar_propiedades():
    """Función que muestra las propiedades del hilo actual, duerme y termina."""
    hilo_actual = threading.current_thread()
    print(f"Nombre del hilo: {hilo_actual.name}")
    print(f"ID del hilo: {hilo_actual.ident}")
    print(f"¿Es daemon?: {hilo_actual.daemon}")
    print(f"¿Está vivo?: {hilo_actual.is_alive()}")
    print("Durmiendo por 5 segundos...")
    time.sleep(5)
    print(f"{hilo_actual.name} ha terminado.")

def main():
    # Crear los hilos
    hilo1 = threading.Thread(target=mostrar_propiedades, name="Hilo-1")
    hilo2 = threading.Thread(target=mostrar_propiedades, name="Hilo-2")

    # Iniciar los hilos
    hilo1.start()
    hilo2.start()

    # Esperar a que terminen los hilos
    hilo1.join()
    hilo2.join()

    print("Todos los hilos han terminado.")

if __name__ == "__main__":
    main()

