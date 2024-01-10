# Encapsulation
class Shaxs:
    def __init__(self, ism, yosh, idcard):
        self.ism = ism
        self.yosh = yosh
        self.__idcard = idcard


shaxs = Shaxs("Anvar", 24, "AB23567")
print(shaxs.idcard)
