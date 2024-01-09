# Polymorphism (Ko'p shakllilik) # noqa
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def info(self):
        return self.name, self.age


class student(Person):
    def __init__(self, name, age, username, id):
        super().__init__(name, age)
        self.username = username
        self.id = id

    def info(self):
        return self.username, self.id, self.name, self.age


one = student('Said', 18, "@said007", 402)
print(*one.info())
