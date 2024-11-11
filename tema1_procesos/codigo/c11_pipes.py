import os

def fork_and_pipe():
    # Crear un pipe (devuelve dos file descriptors: uno para leer, otro para escribir)
    r, w = os.pipe()

    pid = os.fork()

    if pid > 0:
        # Proceso padre
        os.close(r)  # Cerramos el extremo de lectura en el padre
        
        message = "Hola desde el proceso padre"
        print(f"Padre (PID: {os.getpid()}) enviando mensaje: '{message}'")
        
        # Escribir mensaje en el pipe
        os.write(w, message.encode())  # Convertimos el mensaje a bytes
        os.close(w)  # Cerramos el extremo de escritura después de escribir
        
        # Esperar a que el proceso hijo termine
        os.wait()

    else:
        # Proceso hijo
        os.close(w)  # Cerramos el extremo de escritura en el hijo
        
        # Leer desde el pipe usando os.read
        message_received = os.read(r, 1024)  # Leer hasta 1024 bytes del pipe
        os.close(r)  # Cerramos el extremo de lectura después de leer
        
        # Decodificamos el mensaje recibido de bytes a string
        print(f"Hijo (PID: {os.getpid()}) recibió el mensaje: '{message_received.decode()}'")


if __name__ == "__main__":
    fork_and_pipe()

