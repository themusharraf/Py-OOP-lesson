# Inheritance (Meros) # noqa
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class student(Person):
    def __init__(self, name, age, username, id):
        super().__init__(name, age)
        self.username = username
        self.id = id


one = student('Said', 18, "@said007", 402)
