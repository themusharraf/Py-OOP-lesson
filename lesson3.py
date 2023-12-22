class Point:
    def __init__(self):
        self.res = []

    def add_data(self, *args):
        for x in args:
            self.res.append(x)

    def get_res(self):
        return self.res


points = Point()
points.add_data("Aziz", "Jmashid", "Botir")
print(points.get_res())
