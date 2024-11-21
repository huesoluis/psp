import os

def download_with_exec():
    url = "http://tinycorelinux.net/13.x/x86/release/Core-current.iso"
    print("Descargando con exec...")
    os.execlp("wget", "wget", url)

if __name__ == "__main__":
    download_with_exec()

