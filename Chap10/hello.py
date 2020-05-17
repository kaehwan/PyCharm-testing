#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main(x,y):
    # Use try except to catch specific error instead of the system printing
    # out whole list of tracebacks
    try:
        x = int(x)
        y = int(y)
        z = x/y
    except ValueError:
        print("I caught a ValueError")
    except ZeroDivisionError:
        print("Cannot divide a number by zero")
    except: # we can also not specify any error type in try-except
        print("Unknown error")
    else:
        print("Good job")
        print("The answer of {} divided by {} is {}".format(x, y, z))

if __name__ == '__main__':
    main(200, 500)
