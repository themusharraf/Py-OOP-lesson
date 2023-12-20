class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    @property
    def get_info(self):
        return self.name, self.model, self.color


class Malibu(Car):
    def __init__(self, name, model, year, speed, km, color):
        super().__init__(name, model, color)
        self.km = km
        self.year = year
        self.speed = speed

    @property
    def get_info(self):
        return self.name, self.model, self.color, self.km, self.speed, self.year


obj = Malibu("Malibu ", "XL", 2023, 500, 10_000, "black")
print(*obj.get_info)
