#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.swapcase())
print('Hello, World.'.lower())
print('Hello, World.'.upper())


class RevStr(str):
    def __str__(self):
        return self[::-1]


s = RevStr("Hello, world")
print(s)
