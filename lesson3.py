# class Point:
#     def __init__(self):
#         self.res = []
#
#     def add_data(self, *args):
#         for x in args:
#             self.res.append(x)
#
#     def get_res(self):
#         return self.res
#
#
# points = Point()
# points.add_data("Aziz", "Jmashid", "Botir")
# print(points.get_res())


class Shaxs:
    def __init__(self, ism, famlily, age, passport, gender):
        self.ism = ism
        self.famlily = famlily
        self.age = age
        self.passport = passport
        self.gender = gender

    def get_passport(self):
        return self.passport


obj = Shaxs("Akbar", "Akbarov", 27, "AB123434", "Male")


class Student(Shaxs):
    def __init__(self, student_id, student_username, ism, famlily, age, passport, gender):
        super().__init__(ism, famlily, age, passport, gender)
        self.student_id = student_id
        self.student_username = student_username

    def get_passport(self):
        return self.student_username, self.student_username, self.passport


child = Student(4467788, "admin@", "Jasmina", "Alimova", 18, "AD34567", "Female")
print(child.get_passport())
