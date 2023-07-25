#!/usr/bin/env python3
def fibonacci_sequence(n):    
    fib_list = []
    a, b = 0, 1
    while a <= n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list
# print(fibonacci_sequence(6))