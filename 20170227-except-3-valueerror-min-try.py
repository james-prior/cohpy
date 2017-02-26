#!/usr/bin/env python3

'''This program has no try/except sins.

Because the except is not bare and does not specify KeyboardInterrupt,
one can get out of the program by typing ^C,
which spews diagnostic stuff when quitting.
'''

from functools import partial

prompt = 'Please enter an integer: '
for s in iter(partial(input, prompt), None):
    try:
        # This try clause has minimal code. That is good!
        i = int(s)
    except ValueError:
        print('ERROR: That was not an integer. Try again.')
    else:
        print(f'Got {i}. That is a valid integer.')
