class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return self.name, self.age


class B(A):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age

    def info(self):
        return self.name, self.age
