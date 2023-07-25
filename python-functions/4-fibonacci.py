#!/usr/bin/env python3
def fibonacci_sequence(n):     
    fib_list = []
    a, b = 0, 1
    if a<n:
        fib_list.append(a)
        a, b = b, a + b 
        while a<=n:   
         fib_list.append(a)
         a, b = b, a + b        
        return fib_list    
    return fib_list
# print(fibonacci_sequence(4181))