#!/usr/bin/python3
def best_score(a_dictionary):
    return max(a_dictionary.items())[0] if a_dictionary is not None else None
