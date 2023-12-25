from uuid import uuid4


class Author:
    def __init__(self, name, age, gender, password, id=None):
        self.id = uuid4()
        self.name = name
        self.__age = age
        self.gender = gender
        self.__password = password


object = Author("Musharraf", 23, "Male", "Alls90")

nums = list(range(1, 31))
for num in nums:

    if num % 2 != 0:
        print(num)
    else:
        print("Even")