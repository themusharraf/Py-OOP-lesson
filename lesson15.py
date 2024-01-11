"""
Polymorphism
1 ->  overloading
2 -> overriding
"""

# class Calculator:
#     def add(self, a, b):
#         print(a + b)
#
#     def add(self, a, b, c):
#         print(a + b + c)
#
#
# obj = Calculator()
# obj.add(2, 4, 4)

a = 4
a = 5

# print(a)

# overriding
class Calculator:
    def add(self, a, b):
        return a + b

class Phone(Calculator):
    def __init__(self,number):
        super().__init__()
        self.number = number

    def add(self, a, b):
        return a - b

con = Phone(2)
print(con.add(7,5))