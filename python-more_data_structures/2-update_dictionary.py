#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Update the value if the key alreay exists and if it doesn't exist, create.
    a_dictionary[key] = value
    return a_dictionary