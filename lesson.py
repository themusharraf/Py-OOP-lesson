class Student:
    def __init__(self, name, username, age):
        self.name = name
        self.username = username
        self.age = age

    @staticmethod
    def to_upper(name):
        return name.upper()


student = Student("akbar", "ak47", 20)
print(student.name)
print(student.to_upper(name="akbar"))

# Akbar
