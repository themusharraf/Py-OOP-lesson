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

    @property
    def age(self):
        return 2023 - self.year


student = Student("Akbar", "Alimov", 2008, "Tashkent", "007", "@akbar9", "Ass888", "PDP")
print(student.age)
