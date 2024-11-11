import os

def download_tiny_core_os_system():
    """
    Descarga Tiny Core Linux usando os.system().
    """
    os.system("wget http://tinycorelinux.net/12.x/x86/release/TinyCore-current.iso")

if __name__ == "__main__":
    download_tiny_core_os_system()

