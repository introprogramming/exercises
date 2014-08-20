'''An iterative version, perhaps more intuitive for beginners.'''

input = int(raw_input("Enter a number: "));

def next_fibonacci(stop_after):
    """Iteratively searches for the fibonacci number that
    comes after the stop_after value"""
    if stop_after <= 0:
         return 0;
    if stop_after <= 2:
	return 1;
	
    prev = 1;
    curr = 1;
    count = 2;
    
    while count <= stop_after:
        curr = curr + prev;
        prev = curr - prev;
        count = count + 1;
    
    return prev;
    
print next_fibonacci(input);
