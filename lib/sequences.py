#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  # If the length is 0 or negative, print an empty list.
        return
    
    # Initialize the Fibonacci sequence
    fibonacci = [0, 1]
    
    # Generate the Fibonacci sequence up to the desired length
    while len(fibonacci) < length:
        next_value = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_value)
    
    # Print the list up to the desired length
    print(fibonacci[:length])
pass