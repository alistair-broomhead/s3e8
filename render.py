#!/usr/bin/env python
from collections import namedtuple
import sys
from time import sleep
import math, cmath
from termcolor import colored

coord = namedtuple('coord', 'x y')

CENTER = coord(-0.77568377, 0.13646737)
SCALE = coord(0.0002, 0.0002)


DISPLAY = [
    ' ',
    colored('.', 'grey', attrs=['bold']),
    colored(':', 'white'),
    colored(';', 'cyan'),
    colored('*', 'green'),
    colored('0', 'yellow'),
    colored('&', 'red'),
    colored('%', 'magenta'),
    colored('@', 'blue'),
    colored('$', 'cyan', 'on_blue'),
    '#',
]



# maps a pixel (x,y) into a (x,y) point on the Mandelbrot canvas
#def lmap(n, (a,b)): return n/200.0 * (b-a) + a


def lmap(x, y, zoom):
    return complex(x * zoom + CENTER.x, y * zoom + CENTER.y)


def value(x, y, zoom):
    z, c = 0, lmap(x, y, zoom)
    iters = 0
    while cmath.polar(z)[0] < 4 and iters < 1000:
        z = z*z + c
        iters += 1
    return int(math.log(iters)/math.log(1000) * 10.0)


def _render(text, compl, zoom):
    out = sys.stdout
    for r in xrange(-35, 35):
        for c in xrange(-40, 40):
            out.write(DISPLAY[value(r,c,zoom)])
        out.write('\n')


def render(text, compl):
    zoom = 1.0
    while True:
        _render(text, compl, zoom)
        sleep(1)
        zoom *= 0.5


if __name__ == '__main__':
    render('hello', 1+2j)

