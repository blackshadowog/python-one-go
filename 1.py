# 2-D vector class
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"Vector2D: ({self.x}, {self.y})")



# 3-D vector class (inherits from Vector2D)
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)  # Call parent constructor
        self.z = z

    def display(self):
        print(f"Vector3D: ({self.x}, {self.y}, {self.z})")



# Example usage
v2 = Vector2D(3, 4)
v2.display()


v3 = Vector3D(1, 2, 2)
v3.display()

