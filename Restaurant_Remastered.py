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
