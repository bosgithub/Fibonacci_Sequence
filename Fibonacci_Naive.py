'''Fibonacci naive algorithm'''


def Fibonacci(n):
    # Initializing the first 2 entries
    if n <= 1:
        return n
    # Any subsequent number is the sum of the previous two
    return Fibonacci(n-1) + Fibonacci(n-2)
