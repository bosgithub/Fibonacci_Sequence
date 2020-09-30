'''Improved algorithm to quickly find the nth number in the fibonacci sequnce
   this is done using a memoization metheod'''


# Initialize a dictionary
fibonacci_cache = {}


def fibonacci_memo(input_value):
    # Check if the entry is already in our defined dictionary
    if input_value in fibonacci_cache:
        # if so, we just retrieve it
        return fibonacci_cache[input_value]
    # Initialize the first 2 entries
    if input_value == 1:
        value = 1

    elif input_value == 2:
        value = 1
    # Any sunsequent entry is the sum of the previous two
    elif input_value > 2:
        value = fibonacci_memo(input_value - 1) + \
            fibonacci_memo(input_value - 2)
    # Dont forget to put any new computed value into our dictionary
    fibonacci_cache[input_value] = value

    return value


# Simpler code, does what is explained above using a list instead of dictionary
def fast_fibonacci(n):
    a = [0, 1]
    for x in range(2, n+1):
        a.insert(x, a[x - 1] + a[x - 2])
    return a[n]
