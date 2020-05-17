#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
"""
In python, everything is an object
and a class is how an object is defined

An instance of a class is called an object,
it is created by calling the class itself as if it were a function
"""
class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

def main():
    donald = Duck("Ali", 17, "black")
    print(donald.age)
    donald.quack()
    donald.move()

if __name__ == '__main__': main()
