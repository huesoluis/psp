import threading

# Variables globales para almacenar las áreas parciales
areas = [0, 0, 0, 0]

# Función para calcular el área de un triángulo
def area_triangulo(base, altura, indice):
    areas[indice] = (base * altura) / 2

# Función para calcular el área de un rectángulo
def area_rectangulo(base, altura, indice):
    areas[indice] = base * altura

def main():
    # Crear hilos para calcular las áreas de las diferentes secciones
    hilos = []

    # Triángulo izquierdo (base=10 m, altura=12 m)
    hilos.append(threading.Thread(target=area_triangulo, args=(10, 12, 0)))

    # Rectángulo central (base=8 m, altura=12 m)
    hilos.append(threading.Thread(target=area_rectangulo, args=(8, 12, 1)))

    # Rectángulo pequeño derecho (base=6 m, altura=5 m)
    hilos.append(threading.Thread(target=area_rectangulo, args=(6, 5, 2)))

    # Triángulo derecho (base=6 m, altura=5 m)
    hilos.append(threading.Thread(target=area_triangulo, args=(6, 5, 3)))

    # Iniciar los hilos
    for hilo in hilos:
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    # Sumar todas las áreas
    area_total = sum(areas)
    print(f"El área total del polígono es: {area_total} m²")

if __name__ == "__main__":
    main()

