from models.ingredient import Ingredient
import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish_pizza1 = Dish('pizza mussarela', 27.99)
    dish_pizza2 = Dish('pizza calabresa', 27.99)
    dish_invalid = Dish('', 27.99)

    # assert que instancias de ingredientes existem
    assert dish_pizza1 == dish_pizza1
    assert dish_pizza1 != dish_pizza2
    assert dish_invalid.name == ''

    # assert representação dos Ingredients
    assert dish_pizza1.__repr__() == "Dish('pizza mussarela', R$27.99)"

    # assert hashes de ingredientes
    assert dish_pizza1.__hash__() == dish_pizza1.__hash__()
    assert dish_pizza1.__hash__() != dish_pizza2.__hash__()

    # assert método add_ingredient
    dish_pizza1.add_ingredient_dependency(Ingredient('farinha'), 10)
    dish_pizza1.add_ingredient_dependency(Ingredient('agua'), 10)
    dish_pizza1.add_ingredient_dependency(Ingredient('sal'), 5)
    dish_pizza1.add_ingredient_dependency(Ingredient('tomate'), 10)
    dish_pizza1.add_ingredient_dependency(Ingredient('mussarela'), 20)

    assert dish_pizza1.get_ingredients() == set([Ingredient('farinha'),
                                                 Ingredient('agua'),
                                                 Ingredient('sal'),
                                                 Ingredient('tomate'),
                                                 Ingredient('mussarela'),
                                                 ])
    assert dish_pizza1.get_restrictions() != set('')

    # assert dos TypeError e ValueError
    with pytest.raises(TypeError):
        Dish('pizza mussarela', 'R$5.00')

    with pytest.raises(ValueError):
        Dish('pizza mussarela', -5.00)
