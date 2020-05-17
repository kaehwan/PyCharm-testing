#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# All functions return a value
def main():
    kitten(8)
    x = puppy()
    return x


def kitten(x: object = 0, y: object = 0, z: object = 0) -> object:
    print('Meow.' * x)
    print(y, z)


def puppy():
    print("Wow")


if __name__ == '__main__': main()
