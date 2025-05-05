class Car:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

    def __repr__(self):
        return f"{self.year} {self.brand} ({self.color})"


class CarInventory:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def get_cars_by_brand(self, brand):
        return [car for car in self.cars if car.brand.lower() == brand.lower()]  # Fixed typo

    def get_cars_by_year(self, year):
        return [car for car in self.car if car.year == year]  # Fixed typo

    def get_cars_by_color(self, color):
        return [car for car in self.cars if car.color.lower() == color.lower()]


if __name__ == "__main__":
    inventory = CarInventory()

    car1 = Car("BMW", 2020, "Red")
    inventory.add_car(car1)

    print("Cars by year 2020:", inventory.get_cars_by_year(2020))
