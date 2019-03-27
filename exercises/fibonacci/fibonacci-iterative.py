'''An iterative version, perhaps more intuitive for beginners.'''

input = int(input("Enter a number: "))


def fibonacci_n(stop_after):
    """Iteratively searches for the N-th fibonacci number"""
    if stop_after <= 0:
        return 0
    if stop_after <= 2:
        return 1

    prev = 1
    curr = 1
    count = 2

    while count <= stop_after:
        curr = curr + prev
        prev = curr - prev
        count = count + 1

    return prev


def next_fibonacci(stop_after):
    """Iteratively searches for the fibonacci number that
    comes after the stop_after value"""
    prev = 0
    curr = 1

    while prev <= stop_after:
        curr += prev
        prev = curr - prev

    return prev


print(next_fibonacci(input))
