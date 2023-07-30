#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or not a_dictionary:
        return None

    max_score = None
    max_key = None

    for key, value in a_dictionary.items():
        if max_score is None or value > max_score:
            max_score = value
            max_key = key

    return max_key