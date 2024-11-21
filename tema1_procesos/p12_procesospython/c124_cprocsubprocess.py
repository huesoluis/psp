import subprocess

def download_with_subprocess():
    url = "http://tinycorelinux.net/13.x/x86/release/Core-current.iso"
    print("Descargando con subprocess...")
    subprocess.run(["wget", url])

if __name__ == "__main__":
    download_with_subprocess()

