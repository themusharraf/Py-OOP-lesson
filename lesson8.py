class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_address(self):  # getter
        return self.address

    def set_address(self, new_address):
        self.address = new_address # setter


objects = Person("Alice", "16", "Tashkent")
print(objects.get_address())  # getter for the address

