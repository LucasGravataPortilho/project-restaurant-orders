# Req 3
import csv

from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, encoding="utf-8", newline='') as file:
            dataReader = csv.DictReader(file)

            for line in dataReader:
                dish_name = line['dish']
                dish_price = float(line['price'])
                dish_ingredient = line['ingredient']
                dish_recipe_amount = int(line['recipe_amount'])

                self.dishes.add(Dish(dish_name, dish_price))

                next_dish = next(iter(self.dishes))

                next_dish.add_ingredient_dependency(
                    Ingredient(dish_ingredient),
                    dish_recipe_amount,
                    )
