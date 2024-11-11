import os

def fork_and_pipe_math():
    # Crear dos pipes para la comunicación con los hijos
    r1, w1 = os.pipe()  # Pipe para el hijo 1
    r2, w2 = os.pipe()  # Pipe para el hijo 2

    pid1 = os.fork()  # Crear el primer hijo

    if pid1 == 0:
        # Proceso hijo 1
        os.close(r1)  # Cerramos el extremo de lectura en el hijo 1
        
        # Operación matemática: por ejemplo, sumar 5 + 10
        result_hijo1 = 5 + 10
        print(f"Hijo 1 (PID: {os.getpid()}) calculó: 5 + 10 = {result_hijo1}")
        
        # Enviar el resultado al padre a través del pipe
        os.write(w1, str(result_hijo1).encode())
        os.close(w1)  # Cerrar el extremo de escritura después de escribir
        os._exit(0)  # Salir del hijo después de terminar

    else:
        # Crear el segundo hijo
        pid2 = os.fork()

        if pid2 == 0:
            # Proceso hijo 2
            os.close(r2)  # Cerramos el extremo de lectura en el hijo 2
            
            # Operación matemática: por ejemplo, multiplicar 7 * 3
            result_hijo2 = 7 * 3
            print(f"Hijo 2 (PID: {os.getpid()}) calculó: 7 * 3 = {result_hijo2}")
            
            # Enviar el resultado al padre a través del pipe
            os.write(w2, str(result_hijo2).encode())
            os.close(w2)  # Cerrar el extremo de escritura después de escribir
            os._exit(0)  # Salir del hijo después de terminar

        else:
            # Proceso padre
            os.close(w1)  # Cerramos el extremo de escritura en el padre para el pipe 1
            os.close(w2)  # Cerramos el extremo de escritura en el padre para el pipe 2

            # Leer el resultado del primer hijo
            result1 = int(os.read(r1, 1024).decode())  # Leer y convertir a entero
            os.close(r1)  # Cerrar el extremo de lectura después de leer

            # Leer el resultado del segundo hijo
            result2 = int(os.read(r2, 1024).decode())  # Leer y convertir a entero
            os.close(r2)  # Cerrar el extremo de lectura después de leer

            # Esperar a que los dos hijos terminen
            os.waitpid(pid1, 0)
            os.waitpid(pid2, 0)

            # Calcular la suma de los resultados
            suma_total = result1 + result2
            print(f"Padre (PID: {os.getpid()}) recibió los resultados: {result1} y {result2}")
            print(f"La suma total es: {suma_total}")

if __name__ == "__main__":
    fork_and_pipe_math()

