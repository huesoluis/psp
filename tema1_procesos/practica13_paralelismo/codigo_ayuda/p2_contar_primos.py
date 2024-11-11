def es_primo(numero):
    """Función que determina si un número es primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_primos_en_fichero(fichero):
    """Función que lee un archivo y cuenta la cantidad de números primos."""
    total_primos = 0
    
    # Leer los números del fichero
    with open(fichero, 'r') as f:
        for linea in f:
            try:
                numero = int(linea.strip())
                if es_primo(numero):
                    total_primos += 1
            except ValueError:
                print(f"Valor no válido encontrado: {linea.strip()} (omitido)")
    
    return total_primos

if __name__ == "__main__":
    # Nombre del fichero que contiene los números
    fichero = "long_list"
    # Calcular y mostrar el número total de primos
    total_primos = contar_primos_en_fichero(fichero)
    print(f"Total de números primos en el archivo '{fichero}': {total_primos}")

