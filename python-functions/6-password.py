#!/usr/bin/env python3

def validate_password(password):
    if len(password) < 8:
        return False    
    capital = False
    small = False
    number = False

    for valid in password:
        if valid.isspace():
            return False
        if valid.isupper():
            capital = True
        elif valid.islower():
            small = True
        elif valid.isdigit():
            number = True

    return capital and small and number                  
        
# print(validate_password("password123"))
