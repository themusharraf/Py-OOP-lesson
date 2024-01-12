class Shaxs:
    def __init__(self, name, age, idcard):
        self.name = name
        self.age = age
        self.__idcard = idcard  # Encapsulation


obj = Shaxs("Ali", 19, "AD445577")


# print(obj.age)
# print(obj.name)
# print(obj.idcard)

class Talaba(Shaxs):
    def __init__(self, name, age, idcard, username, id):
        super().__init__(name, age, idcard)
        self.username = username
        self.__id = id  # Encapsulation


talaba = Talaba("Jamshid", 19, "AD445577", "jam@44", 8877)
# print(talaba.username)
# print(talaba.idcard)
# print(talaba.id)
