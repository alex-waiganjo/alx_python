#!/usr/bin/env python3

def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True

    # Check if the number is divisible by any number from 2 to the square root of the number (inclusive).
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# def is_prime(number):
#     if number%2==0:
#         return "True"
#     elif number<=1:
#         return "False"
#     else:
#         return "False"    
# print(is_prime(-5))