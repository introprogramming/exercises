input = int(raw_input("Enter a number: "));
# Alternatively:
# input = input("Enter a number; ");
# The difference is that input() parameter is evaluated as a command,
# whereas raw_input() evaluates the parameter as a string

def next_fibonacci(stop_after):
    """Recursively searches for the fibonacci number that
    comes after the stop_after value"""
    if stop_after < 2:
        return stop_after;
    
    
    # Stop if the sought fibonacci number has been found.
    # (The only reason I chose to look at the previous of the two numbers
    # is that I want it to include 0 as a possible return value as well,
    # which will happen with a negative input value).

    #It's this double-recursion that calculates the same value multiple times.
    return next_fibonacci(stop_after - 1) + next_fibonacci(stop_after - 2)


def next_fibonacci_t(prev, curr, stop_after):
    """Tail-recursive implementation with linear complexity."""
    if (stop_after > 0):
        return next_fibonacci_t(curr, curr + prev, stop_after-1)
    elif (stop_after == 0):
        return curr
    else:
        return 0

print next_fibonacci_t(0, 1, input-1)
#print next_fibonacci(input);
