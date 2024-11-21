import os

def download_with_fork():
    url = "http://tinycorelinux.net/13.x/x86/release/Core-current.iso"
    print("Creando un proceso con fork...")
    pid = os.fork()
    if pid == 0:
        # Proceso hijo
        print("Descargando en el proceso hijo...")
        os.execlp("wget", "wget", url)
    else:
        # Proceso padre
        print(f"El proceso hijo tiene PID {pid}. Esperando a que termine...")
        os.wait()

if __name__ == "__main__":
    download_with_fork()

