def factorial(n):
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result
