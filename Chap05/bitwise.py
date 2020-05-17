#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

"""
These operators operates on bits, they are not logical operators
&: And
|: Or
^: Xor
<<: Shift left
>>: Shift right
"""

x = 0x0a
y = 0x02
z = x & y

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
