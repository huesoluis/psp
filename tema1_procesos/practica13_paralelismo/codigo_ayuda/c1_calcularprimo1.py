import random

def is_prime(n):
    """Función que verifica si un número es primo."""
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_random_numbers(count, start, end):
    """Genera una lista de números aleatorios."""
    return [random.randint(start, end) for _ in range(count)]

def count_primes(numbers):
    """Cuenta cuántos números en la lista son primos."""
    return sum(1 for num in numbers if is_prime(num))

def main():
    # Generar 100 números aleatorios entre 1 y 1,000,000
    #r andom_numbers = generate_random_numbers(50000, 1, 1000000)
    random_numbers = generate_random_numbers(500000, 1, 1000000)
    
    # Contar cuántos de esos números son primos
    prime_count = count_primes(random_numbers)
    
    print(f"Se generaron 100 números aleatorios.")
    print(f"Números primos encontrados: {prime_count}")

if __name__ == "__main__":
    main()

