#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

"""
An iterator is a class that provides a sequence of items, generally used
in a loop
"""


class inclusive_range:
    # __init__ is known as constructor, it creates all the variables and
    # check the arguments
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError(f'expected at least 1 argument, got {numargs}')
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError(f'expected at most 3 arguments, got {numargs}')

        self._next = self._start

    # __iter__ simply recognizes an object as an iterable object
    def __iter__(self):
        return self

    # __next__ is the iteration itself, a construct like the for loop
    # to look for this __next__ function in order to treat this as an iterator
    # and in order to use it for iteration
    def __next__(self):
        if self._next > self._stop:  # if we reach _stop
            raise StopIteration  # we raise the stopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r


def main():
    for n in inclusive_range(2,25,3):
        print(n, end=' ')
    print()


if __name__ == '__main__': main()
