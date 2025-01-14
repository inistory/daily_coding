n =int(input())

def factorial(n):
    result = 1
    if n > 0:
        result = n * factorial(n-1)
    return result

print(factorial(n))