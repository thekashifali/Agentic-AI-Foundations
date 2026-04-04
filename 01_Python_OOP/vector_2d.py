class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Defines what happens when you print the object
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Defines what happens when you use the '+' operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Defines what happens when you call len()
    def __len__(self):
        # Returning the 'magnitude' as an integer for this example
        return int((self.x**2 + self.y**2)**0.5)

# Usage
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)           # Triggers __str__ -> Output: Vector(3, 4)
v3 = v1 + v2        # Triggers __add__ -> Output: Vector(4, 6)
print(len(v1))      # Triggers __len__ -> Output: 5