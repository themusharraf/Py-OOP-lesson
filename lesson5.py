class Point:
    def __new__(cls, x, y):
        instance = super(Point, cls).__new__(cls)
        instance.x = x
        instance.y = y
        return instance

    def get_info(self):
        ...


obj = Point(7, 8)
print(obj.get_info())
