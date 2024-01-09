# Polymorphism (Ko'p shakllilik) # noqa

# Overloading
"""
Overloading, bir sinfdagi biror funksiya yoki
metod nomini bir nechta turdagi argumentlar
bilan o'zgartirish imkoniyatini anglatadi. Misol uchun:
"""


class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


one = Calculator()
print(one.add(1, 3, 4))

# Overriding
"""
Overriding esa ota sinfdagi metodni farzand
sinfda qayta yozishni ifodalaydi. Misol uchun:
"""


class Shape:
    def draw(self):
        print("Drawing a shape")


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # method
#     def info(self):
#         return self.name, self.age
#
#
# class student(Person):
#     def __init__(self, name, age, username, id):
#         super().__init__(name, age)
#         self.username = username
#         self.id = id
#
#
#     def info(self):
#         return self.username, self.id, self.name, self.age
#
#
# one = student('Said', 18, "@said007", 402)
# print(*one.info())
