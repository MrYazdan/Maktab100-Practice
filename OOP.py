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

    def __init__(self, first_name: str, last_name: str) -> None:
        self.id = len(self.__class__.students) + 1
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = False
        # self.name = f"{first_name} {last_name}"

        self.__class__.students.append(self)
        # self.students.append(self)

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
