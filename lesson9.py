from uuid import uuid4


class Author:
    def __init__(self, name, age, gender, password, id):
        self.id = uuid4()
        self.name = name
        self.__age = age
        self.gender = gender
        self.__password = password


object = Author("Musharraf", 23, "Male", "Alls90")
