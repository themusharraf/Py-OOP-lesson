# Super Class metodlarni qayta yozish # noqa
class Shaxs:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    # method
    def info(self):
        return self.ism, self.yosh


class Talab(Shaxs):
    def __init__(self, ism, yosh, idcard, address):
        super().__init__(ism, yosh)
        self.idcard = idcard
        self.address = address

    # method
    def info(self):
        return self.ism, self.yosh, self.idcard, self.address


# obyekt
talab = Talab("Gulzoda", 19, "AB2562737", "Tashkent")
print(talab.address)
print(*talab.info())
