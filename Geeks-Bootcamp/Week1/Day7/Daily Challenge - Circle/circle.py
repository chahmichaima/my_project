import math
class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self._radius = float(radius)
        elif diameter is not None:
            self._radius = float(diameter) / 2.0
        else:
            self._radius = 1.0  
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        self._radius = float(value)
    @property
    def diameter(self):
        return self._radius * 2.0
    @diameter.setter
    def diameter(self, value):
        self._radius = float(value) / 2.0
    def compute_area(self):
        return math.pi * (self._radius ** 2)
    def __str__(self):
        return f"Circle(radius={self._radius}, diameter={self.diameter})"
    def __repr__(self):
        return self.__str__()
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self._radius + other._radius)
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self._radius < other._radius
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, Circle):
            return self._radius <= other._radius
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self._radius > other._radius
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, Circle):
            return self._radius >= other._radius
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self._radius == other._radius
        return NotImplemented
# ==========================================
#  (Testing the Circle class)
# ==========================================
if __name__ == "__main__":
    c1 = Circle(radius=3)
    c2 = Circle(diameter=10) 
    c3 = Circle(radius=2)

    print("--- 1.tester ---")
    print(c1)
    print(f"C2 Radius: {c2.radius}, Diameter: {c2.diameter}")
    print(f"Area of c1: {c1.compute_area():.2f}")

    print("\n--- 2. tester l'addition(Dunder __add__) ---")
    c4 = c1 + c3 
    print(f"c1 + c3 = {c4}")
    print("\n--- 3.tester la comparaison---")
    print(f"Is c1 bigger than c3? {c1 > c3}")
    print(f"Are c1 and c3 equal? {c1 == c3}")
    print("\n--- 4. tester l'ordre(Sorting) ---")
    circles_list = [Circle(5), Circle(1), Circle(3), Circle(7.5)]
    print("Before sorting:", circles_list)
    circles_list.sort() 
    print("After sorting:", circles_list)