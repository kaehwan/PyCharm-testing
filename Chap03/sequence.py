#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ]

x[4] = "4+1"

for i in x:
    print('i is {}'.format(i), type(i))

x = {'one': 1,
     'two': 2,
     'three': 3,
     'four': 4,
     'five': 5
     }

for k, v in x.items():
    print(k, v)

x = (1, 'two', 3.0, ['four', 4], 5)
y = ('one', 2, 3.0, ['four', 4], 'v')
print('type of x: {};\nid of x: {}'.format(type(x), id(x)))
print('type of x[1]: {};\nid of x[1]: {}'.format(type(x[1]), id(x[1])))
if x[2] == y[2]:
    print("yep")
else:
    print("nope")


if isinstance(x, tuple):
    print("tuple")
else:
    print("nope")