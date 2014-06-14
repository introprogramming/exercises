'''An iterative version, perhaps more intuitive for beginners.'''

input = int(raw_input("Enter a number: "));

def next_fibonacci(stop_after):
    prev = 0;
    curr = 1;
    
    while prev <= stop_after:
        curr += prev;
        prev = curr - prev;
    
    return prev;
    
print next_fibonacci(input);