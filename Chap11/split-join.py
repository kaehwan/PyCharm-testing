#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
print(s)

# split a string
l = s.split()
print(l)

# split by a specific character
print(s.split("i"))

# join a list into string
s2 = ":".join(l)
print(s2)