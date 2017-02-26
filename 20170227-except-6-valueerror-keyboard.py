#!/usr/bin/env python3

'''This program has no try/except sins.
(At least, not that I am aware of.)

Refactored to have try/except block for KeyboardInterrupt
at highest level,
so catch them regardless of when they happen.

Because KeyboardInterrupt exception is explicitly caught,
one can get out of the program by typing ^C,
and gracefully exit without spewing diagnostics.
'''

from functools import partial

def process_input(s):
    try:
        # This try clause has minimal code. That is good!
        i = int(s)
    except ValueError:
        print('ERROR: That was not an integer. Try again.')
    else:
        print(f'Got {i}. That is a valid integer.')

def main():
    prompt = 'Please enter an integer: '
    for s in iter(partial(input, prompt), None):
        process_input(s)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
