#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) is not 0:
        return max(a_dictionary.items())[0]
