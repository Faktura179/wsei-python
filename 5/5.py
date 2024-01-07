import time

def timed(function):
    def wrapper(*args):
        start = time.time()
        wynik = function(*args)
        end = time.time()
        print(f"Czas wykonania funkcji {function.__name__}: {end - start} sekund")
        return wynik
    return wrapper


@timed
def iterative(n):
    if n < 1:
        raise ValueError("Liczba musi być dodatnia")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

@timed
def recursive(n):
    if n < 1:
        raise ValueError("Liczba musi być dodatnia")
    if n == 1:
        return 1
    return recursive(n - 1) * n

print(iterative(4))
print(recursive(4))