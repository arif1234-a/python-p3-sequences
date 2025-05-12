#!/usr/bin/env python3

import sys
import io

def print_fibonacci(length):
    if length == 0:
        print([])  # Matches expected output
        return

    fibonacci = [0, 1] if length > 1 else [0]
    
    for _ in range(2, length):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    print(fibonacci)  # Prints the correct list format

# Test run:
print_fibonacci(10)