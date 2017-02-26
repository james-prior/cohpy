#!/usr/bin/env python3

'''This program has one try/except sin:
1. too much stuff in try: clause
See https://www.python.org/dev/peps/pep-0008/#programming-recommendations.

Because the except is not bare and does not specify KeyboardInterrupt,
one can get out of the program by typing ^C,
which spews diagnostic stuff when quitting.
'''

from functools import partial

prompt = 'Please enter an integer: '
while True:
    try:
        for i in map(int, iter(partial(input, prompt), None)):
            print(f'Got {i}. That is a valid integer.')
    except ValueError:
        print('ERROR: That was not an integer. Try again.')
