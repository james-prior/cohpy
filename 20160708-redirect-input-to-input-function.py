#!/usr/bin/env python3
'''This program successfully redirects standard input
for the input() function.'''

import sys
import io
from functools import partial

data = '''hello
moby foo
quit
123.456
'''

print(io.StringIO(data).read(), end='')

print('before %r' % sys.stdin)
backup = sys.stdin
with io.StringIO(data) as sys.stdin:
    print('top inside %r' % sys.stdin)
    prompt = 'gimme: '
    for s in iter(partial(input, prompt), 'quit'):
        print(s)
print('after %r' % sys.stdin)
sys.stdin = backup
print('after restoring from backup %r' % sys.stdin)
