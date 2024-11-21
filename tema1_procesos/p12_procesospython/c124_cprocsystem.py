import os

def download_with_system():
    url = "http://tinycorelinux.net/13.x/x86/release/Core-current.iso"
    print("Descargando con os.system...")
    os.system(f"wget {url}")

if __name__ == "__main__":
    download_with_system()

