"""
Polymorphism
1 ->  overloading
2 -> overriding
"""


class Calculator:
    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):
        print(a + b + c)


obj = Calculator()
# obj.add(2, 4, 4)

a = 4
a = 5
# print(a)