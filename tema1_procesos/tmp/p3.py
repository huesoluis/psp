import multiprocessing

def suma_array(array, cola):
    suma = sum(array)
    cola.put(suma)  # Poner el resultado en la cola

if __name__ == '__main__':
    # Array a sumar
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Dividir el array en dos partes
    mitad = len(array) // 2
    parte1 = array[:mitad]
    parte2 = array[mitad:]

    # Crear una cola para almacenar los resultados de los hijos
    cola = multiprocessing.Queue()

    # Crear dos procesos
    p1 = multiprocessing.Process(target=suma_array, args=(parte1, cola))
    p2 = multiprocessing.Process(target=suma_array, args=(parte2, cola))

    # Iniciar los procesos
    p1.start()
    p2.start()

    # Esperar a que los procesos terminen
    p1.join()
    p2.join()

    # Leer los resultados de la cola
    suma1 = cola.get()
    suma2 = cola.get()

    # Calcular la suma total
    suma_total = suma1 + suma2
    print(f"La suma total es: {suma_total}")

