#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

print('This is python version {}'.format(platform.python_version()))


def main():
    message()


def message():
    print("This is the python version {}".format(platform.python_version()))


if __name__ == "__main__":
    main()
