#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

"""
and: And
or: Or
not: Not
in: Value in set
not in: Value not in set
is: Same object identity
is not: Not same object identity
"""

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')

z = "bunny"
if z in x:
    print("True")

if z is y:
    print("z is y")
else:
    print("z is not y")