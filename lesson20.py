from abc import ABC


class Users(ABC):
    def __init__(self, name, username, password, phone, user_type):
        self.name = name
        self.username = username
        self.password = password
        self.phone = phone
        self.user_type = user_type


obj = Users("Ali", "@ali44", "555555555", "998887744", "User")
obj2 = Users("Alice", "@alice", "999999", "778887744", "Staff")
print(obj.name, obj.user_type)
print(obj2.name, obj2.user_type)
