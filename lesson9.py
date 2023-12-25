class Author:
    def __init__(self, name, age, gender, password):
        self.name = name
        self.__age = age
        self.gender = gender
        self.__password = password


object = Author("Musharraf", 23, "Male", "Alls90")
