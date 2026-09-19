import math

class Calculator:
    def square(self, num):
        return num ** 2

    def cube(self, num):
        return num ** 3

    def square_root(self, num):
        return math.sqrt(num)

# Example usage:
a = Calculator()

num = 9
print(f"Square of {num}: {a.square(num)}")
print(f"Cube of {num}: {a.cube(num)}")
print(f"Square root of {num}: {a.square_root(num)}")

