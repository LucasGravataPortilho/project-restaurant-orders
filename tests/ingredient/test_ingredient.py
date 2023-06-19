from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    correct_ingredient = Ingredient('queijo prato')
    wrong_ingredient = Ingredient('presunto')
    invalid_ingredient = Ingredient('')

    # assert que instancias de ingredientes existem
    assert correct_ingredient == correct_ingredient
    assert correct_ingredient != wrong_ingredient
    assert invalid_ingredient.name == ''

    # assert se ingredientes tem alguma restrição
    assert correct_ingredient.restrictions == set()

    # assert hashes de ingredientes
    assert correct_ingredient.__hash__() == correct_ingredient.__hash__()
    assert correct_ingredient.__hash__() != wrong_ingredient.__hash__()

    # assert representação dos Ingredients
    assert correct_ingredient.__repr__() == "Ingredient('queijo prato')"
