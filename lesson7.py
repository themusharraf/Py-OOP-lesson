"""

class Point:
name = None
Point.name

"""


class Point:
    name = None

    @classmethod
    def change_name(cls, newname):
        Point.name = newname


