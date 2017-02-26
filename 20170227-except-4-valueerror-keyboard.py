#!/usr/bin/env python3

'''This program has no try/except sins.

Because KeyboardInterrupt exception is explicitly caught,
one can get out of the program by typing ^C,
and gracefully exit without spewing diagnostics.
'''

from functools import partial

prompt = 'Please enter an integer: '
while True:
    try:
        # This try clause has minimal code. That is good!
        s = input(prompt)
    except KeyboardInterrupt:
        print()
        break
    
    try:
        # This try clause has minimal code. That is good!
        i = int(s)
    except ValueError:
        print('ERROR: That was not an integer. Try again.')
    else:
        print(f'Got {i}. That is a valid integer.')
