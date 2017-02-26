#!/usr/bin/env python3

'''This program has no try/except sins.

Refactored to put each try/except block in a separate function.

Because KeyboardInterrupt exception is explicitly caught,
one can get out of the program by typing ^C,
and gracefully exit without spewing diagnostics.
'''

from functools import partial

def get_input(prompt):
    try:
        # This try clause has minimal code. That is good!
        s = input(prompt)
    except KeyboardInterrupt:
        print()
        s = None
    return s

def process_input(s):
    try:
        # This try clause has minimal code. That is good!
        i = int(s)
    except ValueError:
        print('ERROR: That was not an integer. Try again.')
    else:
        print(f'Got {i}. That is a valid integer.')

prompt = 'Please enter an integer: '
for s in iter(partial(get_input, prompt), None):
    process_input(s)
