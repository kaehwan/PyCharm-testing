#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('berlin.jpg', 'rb')   # rb read the input_file as binary mode
    outfile = open('berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(102400)   # choose the buffer size carefully
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
