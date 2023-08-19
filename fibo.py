def fibo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_serie = [0, 1]
        for i in range(2, n):
            next_fib = fib_serie[i-1] + fib_serie[i-2]
            fib_serie.append(next_fib)
        return fib_serie


# Ejemplo
n = 10
fib_serie = fibo(n)
print(f"Los primeros {n} numeros en la sequencia son: {fib_serie}")
