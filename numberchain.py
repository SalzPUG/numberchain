#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial
from itertools import permutations


def determine_key(val, multiplier):
    val_as_string = str(val)
    return val_as_string * (multiplier / len(val_as_string) + 1)
    

def numberchain(*numbers):
    """Arrange non-negative integers to build the largest possible number."""
    multiplier = len(str(max(numbers)))
    key_function = partial(determine_key, multiplier=multiplier)
    sorted_numbers = reversed(sorted(numbers, key=key_function))
    return int("".join(str(n) for n in sorted_numbers))


def correct_solution(*numbers):
    highscore = 0
    for permutation in permutations(numbers):
        score = int(''.join(str(n) for n in permutation))
        if score > highscore:
            highscore = score
    return highscore
    
    
def reference_implementation(*numbers):
    def comp_func(a, b):
        return cmp(str(a)+str(b), str(b)+str(a))
    sorted_numbers = reversed(sorted(numbers, cmp=comp_func))
    return int("".join(str(n) for n in sorted_numbers))
    

if __name__ == "__main__":
    import nose
    nose.main()
