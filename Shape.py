import math

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

    def compute_distance(self, other):
        if not isinstance(other, Point):
            raise TypeError("Argument must be a Point instance.")
        return math.sqrt((self._x - other.get_x()) ** 2 + (self._y - other.get_y()) ** 2)

class Line:
    def __init__(self, start, end):
        if not all(isinstance(point, Point) for point in (start, end)):
            raise TypeError("Start and end must be instances of Point.")
        self._start = start
        self._end = end

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def length(self):
        return self._start.compute_distance(self._end)

class Shape:
    def __init__(self, vertices):
        if not all(isinstance(vertex, Point) for vertex in vertices):
            raise TypeError("Vertices must be instances of Point.")
        self._vertices = vertices
        self._edges = [Line(vertices[i], vertices[(i + 1) % len(vertices)]) for i in range(len(vertices))]

    def get_vertices(self):
        return self._vertices

    def get_edges(self):
        return self._edges

    def compute_area(self):
        ...

    def compute_perimeter(self):
        return sum(edge.length() for edge in self._edges)

class Rectangle(Shape):
    def __init__(self, bottom_left, width, height):
        vertices = [
            bottom_left,
            Point(bottom_left.get_x() + width, bottom_left.get_y()),
            Point(bottom_left.get_x() + width, bottom_left.get_y() + height),
            Point(bottom_left.get_x(), bottom_left.get_y() + height)
        ]
        super().__init__(vertices)
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, value):
        self._width = value

    def get_height(self):
        return self._height

    def set_height(self, value):
        self._height = value

    def compute_area(self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self, bottom_left, side_length):
        super().__init__(bottom_left, side_length, side_length)

class Triangle(Shape):
    def __init__(self, vertices):
        if len(vertices) != 3:
            raise ValueError("A triangle must have exactly 3 vertices.")
        super().__init__(vertices)

    def compute_area(self):
        a, b, c = self._vertices
        return abs(a.get_x() * (b.get_y() - c.get_y()) + b.get_x() * (c.get_y() - a.get_y()) + c.get_x() * (a.get_y() - b.get_y())) / 2

    def get_triangle_type(self):
        a, b, c = self._vertices
        ab = a.compute_distance(b)
        bc = b.compute_distance(c)
        ca = c.compute_distance(a)

class Isosceles(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
    
    def is_isosceles(self):
        a, b, c = self._vertices
        ab = a.compute_distance(b)
        bc = b.compute_distance(c)
        ca = c.compute_distance(a)
        return math.isclose(ab, bc) or math.isclose(bc, ca) or math.isclose(ca, ab)


class Equilateral(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
    
    def is_equilateral(self):
        a, b, c = self._vertices
        ab = a.compute_distance(b)
        bc = b.compute_distance(c)
        ca = c.compute_distance(a)
        return math.isclose(ab, bc) and math.isclose(bc, ca)


class Scalene(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
    
    def is_scalene(self):
        a, b, c = self._vertices
        ab = a.compute_distance(b)
        bc = b.compute_distance(c)
        ca = c.compute_distance(a)
        return not (math.isclose(ab, bc) or math.isclose(bc, ca) or math.isclose(ca, ab))


class TriRectangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)

    def is_right_triangle(self):
        a, b, c = self._vertices
        sides = [a.compute_distance(b), b.compute_distance(c), c.compute_distance(a)]
        sides.sort()
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(2, 0)
    p3 = Point(1, 2)

    rect = Rectangle(p1, 4, 3)
    print(f"Rectangle Area: {rect.compute_area()}")
    print(f"Rectangle Perimeter: {rect.compute_perimeter()}")

    square = Square(p1, 4)
    print(f"Square Area: {square.compute_area()}")
    print(f"Square Perimeter: {square.compute_perimeter()}")

    triangle = Triangle([p1, p2, p3])
    print(f"Triangle Area: {triangle.compute_area()}")

    tri_equilateral = Equilateral([p1, p2, p3])
    print(f"Is Equilateral?: {tri_equilateral.is_equilateral()}")

    tri_isosceles = Isosceles([p1, p2, p3])
    print(f"Is Isosceles?: {tri_isosceles.is_isosceles()}")

    tri_scalene = Scalene([p1, p2, p3])
    print(f"Is Scalene?: {tri_scalene.is_scalene()}")

    tri_rectangle = TriRectangle([p1, p2, p3])
    print("Is Right Triangle:", tri_rectangle.is_right_triangle())
