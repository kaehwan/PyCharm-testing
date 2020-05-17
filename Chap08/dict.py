#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = {'kitten': 'meow',
               'puppy': 'ruff!',
               'lion': 'grrr',
               'giraffe': 'I am a giraffe!',
               'dragon': 'rawr'
               }
    print_dict(animals)
    print()
    for k in animals.keys(): print(k)
    print()
    for v in animals.values(): print(v)
    print()
    for k, v in animals.items(): print("{}: {}".format(k, v))
    print()
    print(animals.get("lion"))  # get will find the input key and return the value


def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')


if __name__ == '__main__':
    main()
