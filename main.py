# from colorama import Fore
#
#
# class Car:
#     name = ""
#     color = ""
#     price = 0
#
#
# car = Car()  # object 1
# car.name = "BMW X7"
# car.color = "black"
# car.price = 145_000
#
# car1 = Car()  # object 2
# car1.name = "BMW X"
# car1.color = "Green"
# car1.price = 34_900
#
# print(Fore.RED + "Car name:" + car.name)
# print(Fore.YELLOW + "Car color:", car.color)
# print(Fore.GREEN + "Car price:", car.price)


class Person:
    def __init__(self, name, year, gender, address):
        self.name = name
        self.year = year
        self.gender = gender
        self.address = address

    def get_info(self):
        return self.name, self.year, self.gender, self.address




Odam = Person("Barno", 2000, "qiz", "Tashkent")

print(*Odam.get_info())
