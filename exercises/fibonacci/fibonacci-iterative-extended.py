'''Iterative version that continously asks and answers the user,
 and saves the calculated fibonacci series in case the user asks for something in that range.'''

fibonacci = [0, 1]

def main():
    input = get_input()
    while input != "exit":
        try:
            number = int(input)
        except ValueError:
            print("Please enter a valid integer!")
            input = get_input()
            continue
        if number >= fibonacci[-1]:
            print(next_fibonacci(number))
        else:
            print(find_next_fibonacci(number))
        input = get_input()

def get_input():
    return input("Enter a number or 'exit' to quit: ")

def next_fibonacci(stop_after):
    """Iteratively generates the fibonacci sequence, starting where the currently saved series ends, until the fibonacci number that
    comes after the stop_after value is found"""
    while fibonacci[-1] <= stop_after:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])

    return fibonacci[-1]

def find_next_fibonacci(stop_after):
    """Naively searches the stored list for the fibonacci number that
     comes after the stop_after value"""
    #Binary search would be faster
    for num in fibonacci:
        if num > stop_after:
            return num

if __name__ == "__main__":
    main()