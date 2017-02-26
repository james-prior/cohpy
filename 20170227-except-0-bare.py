#!/usr/bin/env python3

'''This program has two try/except sins:
1. too much stuff in try: clause
2. bare except
See https://www.python.org/dev/peps/pep-0008/#programming-recommendations.

Because of the bare except, one can not get out of the program by typing ^C.

For iter(partial(input, prompt), sentinel) idiom,
see https://mail.python.org/pipermail/centraloh/2016-July/002895.html
and http://nbviewer.jupyter.org/github/james-prior/cohpy/blob/master/20160708-dojo-user-input-loop-with-iter-partial-input-prompt-sentinel.ipynb
.
'''

from functools import partial

prompt = 'Please enter an integer: '
while True:
    try:
        for i in map(int, iter(partial(input, prompt), None)):
            print(f'Got {i}. That is a valid integer.')
    except: # This catches all exceptions, including KeyboardInterrupt.
        print('ERROR: That was not an integer. Try again.')
