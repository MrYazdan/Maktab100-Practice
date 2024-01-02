from random import randint
from typing import NamedTuple


# OOP !
# [ Inheritance - Mixin - Data Hiding (Encapsulation) - Polymorphism - Composite ]
# Property
# Decorator
# Design pattern

# class Student:
#     pass

# sahar = "sahar, "

# sahar = ['sahar',...]

# sahar = {
#     "first_name": 'sahar',
#     "last_name": 'bahrami',
# }

# def student_creator(first_name, last_name):
#     return {
#         "first_name": first_name,
#         "last_name": last_name,
#     }

# def activate(student: dict):
#     student["is_active"] = True
#     return student
#
#
# def student_creator(first_name, last_name):
#     return {
#         "first_name": first_name,
#         "last_name": last_name,
#         "activate": activate
#     }
#
#
# sahar = student_creator("sahar", "bahrami")
# sahra = sahar["activate"](sahar)


# def activate(obj):
#     obj.is_active = True
#
#
# class Student:
#     pass
#
#
# sahar = Student()
# sahar.name = "sahar"
# sahar.family = "bahrami"
# sahar.activate = activate
# sahar.activate(sahar)

# numbers = [1, 34, 5, 756, 0, -10, -6, 324, 2]

# in-place method:
# print(numbers.sort())
# print(numbers)

# out-place method
# print(sorted(numbers))
# print(numbers)


class Student:
    # class attrs
    # name = "Student Class name"
    students = []

    @staticmethod
    def get_random_id():
        return randint(1, 9999)

    @classmethod
    def get_new_id(cls):
        return len(cls.students) + 1

    def __new__(cls, first_name: str, last_name: str):
        # print("__new__ Started !")
        self = super().__new__(cls)
        # print(id(self))
        cls.students.append(self)
        # print("__new__ has End !")
        return self

    def __init__(self, first_name: str, last_name: str) -> None:
        # print("Initializing Started !")

        self.id = len(self.__class__.students)
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = False

        # print(id(self))
        # self.name = f"{first_name} {last_name}"

        # implemented in __new__:
        # self.__class__.students.append(self)
        # self.students.append(self)
        # print("Initializing has End !")

    # in-place method
    def activate(self):
        self.is_active = True

    def __repr__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, __value):
        return self.id == __value

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print(str(self), "is Called !")


sahar = Student("sahar", "bahrami")
reza = Student("reza", "yazdani")

# print(sahar)
# print(reza.name)
# print(sahar.__class__.name)
# print(Student.name)

# print(str(reza))  # => reza.__str__()
# print(reza.__repr__())  # => reza.__str__()
# print(sahar)  # => sahar.__str__()

# reza.id = sahar.id
# print(sahar.id, reza.id)
# print(sahar == reza)

# reza(1, True, 'salam', name="ajab", state=False)

shima = Student("shima", "tehrani")


# shima()
# print(Student.students)

# print(shima.is_active)
# shima.activate()  # => Student.activate(shima)
# print(shima.get_new_id())
# print(shima.is_active)
# Student.get_random_id(shima)
# shima.get_random_id(shima)


# username: is_id , min: 6, max: 12, not-editable !
# password: min(4), max(8), hash(pass)
# class_method => login(user, pass)


# class User:
#     __db = []
#
#     def __new__(cls, first_name: str, last_name: str):
#         self = super().__new__(cls)
#         cls.__db.append(self)
#         return self
#
#     @staticmethod
#     def _username_validator(username):
#         assert isinstance(username, str) and username.isidentifier() and 8 <= len(username) <= 12, "Username not valid"
#         return username
#
#     @staticmethod
#     def _password_validator(password):
#         assert isinstance(password, str) and 4 <= len(password) <= 8, "Password not valid"
#         return password
#
#     @classmethod
#     def login(cls, username, password):
#         for user in cls.__db:
#             if user.authenticate(username, password):
#                 return True
#         return False
#
#     def __init__(self, username, password):
#         self.__username = self._username_validator(username)
#         self.__password = self._password_validator(password)
#
#     def authenticate(self, username, password) -> bool:
#         username = self._username_validator(username)
#         password = self._password_validator(password)
#
#         return self.__username == username and self.__password == password
#
#     def get_password(self):
#         return hash(self.__password)
#
#     def change_password(self, old_pass, new_pass):
#         old_pass = self._password_validator(old_pass)
#         new_pass = self._password_validator(new_pass)
#
#         if old_pass == self.__password:
#             self.__password = new_pass
#
#     @property
#     def username(self):
#         return self.__username
#
#
# yazdan = User("yazdan1234", "565623")
# admin = User("admin1212", "123456")

# Users.login()
# print(yazdan.username)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        assert isinstance(new_username, str) and new_username.isidentifier() and 8 <= len(new_username) <= 12, "Username not valid"
        self.__username = new_username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        assert isinstance(new_password, str) and 4 <= len(new_password) <= 8, "Password not valid"
        self.__password = new_password


yazdan = User("yaz", "565623")
