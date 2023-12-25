class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_address(self):  # getter for the address
        return self.address


objects = Person("Alice", "16", "Tashkent")
print(objects.get_address())  # getter for the address
