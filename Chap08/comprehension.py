#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    print_list(seq)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

a = [x for x in range(100) if x%3==0]
print(a)

# Comprehension is applicable to the generation of dictionary as well
k = ["a", "b", "c", "d", "e", "f"]
v = a[:6]
d = {k: v**2 for k, v in zip(k, v)}
print(d)