#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    pass


def function(n):
    print(n)
    return n*2

x = function(47)
print(x)

def is_prime(x):
    if x <= 1:
        return False
    else:
        if x % 2 == 0:
            return False
        else:
            return True

x = 5

if is_prime(x):
    print('{} is prime.'.format(x))
else:
    print('{} not prime.'.format(x))
    
def list_primes():
    for i in range(100):
        if is_prime(i):
            print(i, end=' ', flush=True)

list_primes()

if __name__ == '__main__': main()