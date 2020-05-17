#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('lines.txt')
    for line in f:
        print(line.rstrip())    # rstrip() will strip any white space including new lines from the end of the line


if __name__ == '__main__': main()

with open("lines.txt", "r") as f:
    for line in f.readlines():
        print(line)


