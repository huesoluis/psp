"""
Explicación del código
    Función es_primo: Determina si un número es primo. Devuelve True si el número es primo y False si no lo es.

Función contar_primos_en_fichero:
    Abre el archivo short_list y lee cada línea.
    Convierte la línea a un número entero.
    Usa es_primo para verificar si el número es primo y, si es así, incrementa el contador total_primos.
    Si encuentra un valor no válido (que no puede convertirse en entero), muestra un mensaje y lo omite.

Bloque principal __main__: Define el nombre del archivo (short_list) y llama a contar_primos_en_fichero para obtener el número total de primos en el archivo, mostrando luego el resultado.
    Este programa asumirá que short_list está en el mismo directorio y contiene una lista de números enteros.
"""

import random

def generar_numeros(fichero, cantidad=500000, rango=(1, 2000000)):
    with open(fichero, 'w') as f:
        for _ in range(cantidad):
            f.write(f"{random.randint(*rango)}\n")

if __name__ == "__main__":
    generar_numeros("long_list")
    print("Fichero generado con 50,000 números aleatorios.")

