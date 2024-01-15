"""
Abstraksiya: Tushunchalar va funksiyalar orqali
kompleks tizimlarni abstrakt ko'rsatish.
Shunday qilib, dastur kodini aniq va qisqa qilish mumkin.
"""
# Abctraction

from abc import ABC, abstractmethod
class Users(ABC):
    def __init__(self, name, username, email, phone, password, user_type):
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password
        self.user_type = user_type
        
    # @abstractmethod
    # def get_user_info(self):
    #     ...


user = Users("ALi", "@ali", "ali@gmail.com", "779996677", "Ajk44", "user")
user1 = Users("Jhon", "@jhon", "jhon@gmail.com", "779988677", "hh44", "staff")
print(user.user_type)
print(user1.user_type)
"""
# Python

1.Abstract Subclass yarating va undan meros olib child class yarating va natijani tekshring.
2.Abstract Propertie class yarating va unda @propertie decorator ishlating .
3.Abstrakt classni yarating va unda @abstractmethod ni ishlating.

homework 12.01.2024 

"""