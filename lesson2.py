class People:
    school_name = "ABC School"

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    @classmethod
    def change_name(cls, name):
        print(People.school_name)
        People.school_name = name


objects = People("Ali", 16, "Tashkent")
People.change_name("PDP School")
print(objects.school_name)
