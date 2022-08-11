from abc import ABC, abstractmethod
from typing import List


class Item(ABC):
    def name(self) -> str:
        pass

    def packing(self) -> "Packing":
        pass

    def price(self) -> float:
        pass


class Packing(ABC):
    def pack(self) -> str:
        pass


class Wrapper(Packing):
    def pack(self) -> str:
        return "Wrapper"


class Bottle(Packing):
    def pack(self) -> str:
        return "Bottle"


class Burger(Item):
    def packing(self) -> "Packing":
        return Wrapper()

    @abstractmethod
    def price(self) -> float:
        pass


class ColdDrink(Item):
    def packing(self) -> "Packing":
        return Bottle()

    @abstractmethod
    def price(self) -> float:
        pass


class VegBurger(Burger):
    def price(self) -> float:
        return 25.0

    def name(self) -> str:
        return "Veg Burger"


class ChickenBurger(Burger):
    def price(self) -> float:
        return 50.5

    def name(self) -> str:
        return "Chicken Burger"


class Coke(ColdDrink):
    def price(self) -> float:
        return 30.0

    def name(self) -> str:
        return "Coke"


class Pepsi(ColdDrink):
    def price(self) -> float:
        return 35.0

    def name(self) -> str:
        return "Pepsi"


class Meal:
    items: List[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)

    def get_cost(self) -> float:
        return sum([item.price() for item in self.items])

    def show_items(self):
        for item in self.items:
            print(f"Item : {item.name()}", end="")
            print(f", Packing : {item.packing().pack()}", end="")
            print(f", Price : {item.price()}")


class MealBuilder:
    def prepare_veg_meal(self) -> Meal:
        meal = Meal()
        meal.add_item(VegBurger())
        meal.add_item(Coke())
        return meal

    def prepare_non_veg_meal(self) -> Meal:
        meal = Meal()
        meal.add_item(ChickenBurger())
        meal.add_item(Pepsi())
        return meal


if __name__ == "__main__":
    meal_builder: MealBuilder = MealBuilder()

    veg_meal: Meal = meal_builder.prepare_veg_meal()
    print("Veg Meal")
    veg_meal.show_items()
    print(f"Total Cost: {veg_meal.get_cost()}")

    non_veg_meal: Meal = meal_builder.prepare_non_veg_meal()
    print("\n\nNone-Veg Meal")
    non_veg_meal.show_items()
    print(f"Total Cost: {non_veg_meal.get_cost()}")
