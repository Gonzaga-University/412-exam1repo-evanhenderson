#!/usr/bin/env python3

import sys

class Adder():
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def getSum(self):
        return self.val1 + self.val2
    def mult(self):
        return self.val1 * self.val2
    def sub(self):
        return self.val1 - self.val2
    def add_mod(self):
        return self.val1 + self.val2 % 2
if __name__ == "__main__":
    print("Starting program")

    adder = Adder(10, 20)
    print(adder.getSum())
    print(adder.mult())
    print(adder.sub())
    print(adder.add_mod())

    print("Done with program")
