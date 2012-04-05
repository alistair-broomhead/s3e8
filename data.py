__author__ = 'al'

import random

class CrazyValue(int):
	def __add__(self, other):
		return self

	__sub__ = __add__
	__mul__ = __add__
	__div__ = __add__

class RandomDict(dict):
	def __getitem__(self, key):
		if key == 'vi':
			return random.choice((True, False))
		return dict.__getitem__(self, key)

def make_func(x):
	def f(y):
		return CrazyValue(x*y)
	return f

data = RandomDict({
    'emacs' : [chr(x) for x in range(256)], #List of strings
    'vi' : True, #bool
    'pony' : {
        '':set(make_func(x) for x in range(10)),
        'fly':set(make_func(-x) for x in range(10))
    },
    'sublime' : open(__file__),
    'santa': 10e100j # some complex number
})