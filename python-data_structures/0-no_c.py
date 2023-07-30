#!/usr/bin/env python3
def no_c(my_string):
    result = ''
    for char in my_string:
        if char not in 'cC':
            result += char
    return result