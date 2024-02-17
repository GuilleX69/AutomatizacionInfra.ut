#!/bin/python
def fibonacci(n):
    fib_series = [0, 1]  # Inicializamos la serie de Fibonacci con los primeros dos números

    # Generamos los siguientes números de la serie
    for i in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)

    return fib_series[:n]

# Pedimos al usuario que ingrese el número de términos de la serie que desea generar
n = int(input("Ingrese el número de términos de la serie de Fibonacci que desea generar: "))

# Generamos la serie de Fibonacci
fib_series = fibonacci(n)

# Imprimimos la serie de Fibonacci
print("La serie de Fibonacci con", n, "términos es:", fib_series)
