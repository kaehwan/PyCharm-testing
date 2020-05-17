#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# print('Hello, World.')

class Bunny():
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f"repr: the number of bunnies is {self._n}"

    def __str__(self):
        return f"str: the number of bunnies is {self._n}"


x = Bunny(47)
print(repr(x))  # repr means representation, it will print the value returned by the special repr method
print(x)
# try to run this python file with or wihout __repr__ in class Bunny

