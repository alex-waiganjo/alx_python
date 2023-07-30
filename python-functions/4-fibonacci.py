#!/usr/bin/env python3
def fibonacci_sequence(n):
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers[:n]

n = 10
fibonacci_numbers = fibonacci_sequence(n)