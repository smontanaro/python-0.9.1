#!/usr/bin/env python

"""A better reconstitution of the original shell archives from the Google HTML files.

Example (for part 09):

curl https://groups.google.com/g/alt.sources/c/w0LgGPVB6f0/m/SDnD377as9IJ \
| egrep '<section>' \
| sed -e 's/.*<section>//' -e 's:</section>.*::' \
| python shar/sharify.py > shar/python-0.9.1-09-21.shar
"""

import html
import re
import sys

shar = sys.stdin.read()

for (pat, repl) in (
        (r'X\t', r'X	'),
        (r'X	\t', r'X		'),
        (r'X		\t', r'X			'),
        (r'X			\t', r'X				'),
        ):
    shar = shar.replace(pat, repl)

for (pat, repl) in (
        (',[2,[[1,[null,"', ''),
        (r'\u0026lt;\u003c', '<'),
        (r'\u003e\u0026gt;', '>'),
        (r'\u003c', '<'),
        (r'\u003d', '='),
        (r'\u003e', '>'),
        (r'\u0026', '&'),
        (r'\"', '"'),
        (r'"]', ''),
):
    shar = shar.replace(pat, repl)

shar = html.unescape(shar)

for (pat, repl) in (
        ('<br>', '\n'),
        ):
    shar = shar.replace(pat, repl)

for (pat, repl) in (
        (r'<a href="[^"]+" target="_blank" rel="nofollow"'
         r' data-saferedirecturl="[^"]+">([^<]+)</a>',
         r'\1'),
        (r'<a href data-email-masked rel="nofollow">([^<]+)</a>', r'\1'),
    ):
    shar = re.sub(pat, repl, shar)

sys.stdout.write(shar.rstrip())
