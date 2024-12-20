# reto_4
## Tabla de Contenido
- [Restaurant](#restaurantremastered)
  - [Python Code](#python-code)
  - [Output](#output)
- [Shape](#shape)
  - [Python Code](#python-code2)
  - [Output](#output)

# RestaurantRemastered
Include the class exercise in the repo.
The restaurant revisted
Add setters and getters to all subclasses for menu item
Override calculate_total_price() according to the order composition (e.g if the order includes a main course apply some disccount on beverages)
Add the class Payment() following the class example.

Se modifico el codigo, se le añadieron setters y getters a las diferentes clases, ademas de añadir el ejemplo de payment hecho en clase, por ultimo se modifico el descuento anterior y ahora si la orden tiene mas de 1 `MainCourse` las bebidas tendran un 30% de descuento.
## Python Code

```python
class MenuItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def calculate_price(self):
        return self._price

    def __str__(self):
        return f"{self._name}: ${self._price:.2f}"


class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size

    def get_size(self):
        return self._size

    def set_size(self, size):
        self._size = size

    def __str__(self):
        return f"{self._name} ({self._size}): ${self._price:.2f}"


class Appetizer(MenuItem):
    def __init__(self, name, price, spicy=False):
        super().__init__(name, price)
        self._spicy = spicy

    def get_spicy(self):
        return self._spicy

    def set_spicy(self, spicy):
        self._spicy = spicy

    def __str__(self):
        spice = "Spicy" if self._spicy else "Non-Spicy"
        return f"{self._name} ({spice}): ${self._price:.2f}"


class MainCourse(MenuItem):
    def __init__(self, name, price, vegetarian=False):
        super().__init__(name, price)
        self._vegetarian = vegetarian

    def get_vegetarian(self):
        return self._vegetarian

    def set_vegetarian(self, vegetarian):
        self._vegetarian = vegetarian

    def __str__(self):
        type_of_dish = "Vegetarian" if self._vegetarian else "Non-Vegetarian"
        return f"{self._name} ({type_of_dish}): ${self._price:.2f}"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def calculate_total(self):
        return sum(item.calculate_price() for item in self.items)

    def calculate_total_price(self):
        total = self.calculate_total()
        main_courses = sum(1 for item in self.items if isinstance(item, MainCourse))
        beverages = [item for item in self.items if isinstance(item, Beverage)]

        if main_courses > 1 and beverages:
            for beverage in beverages:
                total -= 0.3 * beverage.get_price()

        return total

    def print_receipt(self):
        print("Order Receipt:")
        for item in self.items:
            print(f"- {item}")
        subtotal = self.calculate_total()
        total = self.calculate_total_price()
        print(f"\nSubtotal: ${subtotal:.2f}")
        if total < subtotal:
            print(f"Discounted Total: ${total:.2f}")
        else:
            print(f"Total: ${subtotal:.2f}")


class Payment:
    def __init__(self):
        pass

    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement the pay method")


class Card(Payment):
    def __init__(self, number, cvv):
        super().__init__()
        self.number = number
        self.cvv = cvv

    def pay(self, amount):
        print(f"Paying ${amount:.2f} with card ending in {self.number[-4:]}")


class Cash(Payment):
    def __init__(self, amount_given):
        super().__init__()
        self.amount_given = amount_given

    def pay(self, amount):
        if self.amount_given >= amount:
            change = self.amount_given - amount
            print(f"Payment successful. Change: ${change:.2f}")
        else:
            print(f"Insufficient funds. Missing ${amount - self.amount_given:.2f}")


# Ejemplo de uso
if __name__ == "__main__":
    order = Order()
    order.add_item(Beverage("Coke", 2.0, "small"))
    order.add_item(Beverage("Tamarindo", 3.0, "medium"))
    order.add_item(Beverage("Jamaica", 2.5, "Large"))
    order.add_item(Appetizer("Tacos de al pastor", 3.0, True))
    order.add_item(Appetizer("Flauta", 6.5, False))
    order.add_item(MainCourse("Veggie Burrito", 8.0, True))
    order.add_item(MainCourse("Enchilada", 12.0, True))

    order.print_receipt()

    print("\nPayment:")
    payment_method = Card("1234123412341234", 500)
    payment_method.pay(order.calculate_total_price())
```
## Output
```bash
Order Receipt:
- Coke (small): $2.00
- Tamarindo (medium): $3.00
- Jamaica (Large): $2.50
- Tacos de al pastor (Spicy): $3.00
- Flauta (Non-Spicy): $6.50
- Veggie Burrito (Vegetarian): $8.00
- Enchilada (Vegetarian): $12.00

Subtotal: $37.00
Discounted Total: $34.75

Payment:
Paying $34.75 with card ending in 1234
```

# Shape
Create a superclass called Shape(), which is the base of the classes Reactangle() and Square(), define the methods compute_area and compute_perimeter in Shape() and then using polymorphism redefine the methods properly in Rectangle and in Square.
Using the classes Point() and Line() define a new super-class Shape() with the following structure:

Se modifico el codigo, se añadio la clase shape ademas de las "hijas" de `Triangle` es decir equilatero, isoceles y escaleno, ademas de una cuarta que verifica si el triangulo es rectangulo 

## Python Code2
```python
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

```
## Output
```bash
Rectangle Area: 12
Rectangle Perimeter: 14.0
Square Area: 16
Square Perimeter: 16.0
Triangle Area: 2.0
Is Equilateral?: False
Is Isosceles?: True
Is Scalene?: False
Is Right Triangle: False
```
