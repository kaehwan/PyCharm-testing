#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten('meow', 'grrr', 'purr')
    x = ("bark", "horr", "fuck", "jiasai")  # can be a tuple or list
    # without putting an * before x, it will print the whole tuple as one
    kitten(*x)

# *args is the variable length argument list
def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow.')

if __name__ == '__main__': main()
