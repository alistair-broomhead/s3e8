import sys
import math, cmath

RX, RY = (-2.5,1), (-1,1)
 
# maps a pixel (x,y) into a (x,y) point on the Mandelbrot canvas
def lmap(n, (a,b)): return n/200.0 * (b-a) + a
 
def value(x,y):
    x *= 2.5
    y *= 2.5
    z, c = 0, complex(lmap(x, RX), lmap(y, RY))
    iters = 0
    while cmath.polar(z)[0] < 4 and iters < 1000:
        z = z*z + c
        iters += 1
    return int(math.log(iters)/math.log(1000) * 10.0)


def render(text, compl):
    out = sys.stdout #open('out.txt', 'w')
    for r in xrange(60):
        for c in xrange(80):
            out.write(' .:;*0&%@$#'[value(r,c)])
        out.write('\n')

