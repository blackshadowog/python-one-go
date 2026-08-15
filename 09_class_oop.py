class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

student = Student("Alex")
print(student.greet())