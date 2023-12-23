"""

class Point:
name = None
Point.name

"""

"""
class Point:
    name = None

    @classmethod
    def change_name(cls, newname):
        Point.name = newname


print(Point.name)
Point.change_name("PDP point")
print(Point.name)

"""


class Person:
    def __init__(self, firstname, lastname, year, address):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.address = address


class Student(Person):
    def __init__(self, firstname, lastname, year, address, student_id, username, password, university):
        super().__init__(firstname, lastname, year, address)
        self.student_id = student_id
        self.username = username
        self.password = password
        self.university = university


    def age(self):
        ...



student = Student("Akbar", "Alimov", 2008, "Tashkent", "007", "@akbar9", "Ass888", "PDP")
print(student.age)




"""
class Student():

University name
student_id
username
password

"""
