#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

"""
A decorator is a form of metaprogramming and it can be described as a special
type of function that returns a wrapper function
"""
import time


def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')

    return wrapper


@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')


@elapsed_time
def fuck():
    num_list = []
    for i in range(1000000):
        num_list.append(i)
    print("fuck me {} times".format(sum(num_list)))


def main():
    fuck()


if __name__ == '__main__': main()
