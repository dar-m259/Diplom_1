import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestIngredient:

    @pytest.mark.parametrize('type, name, price', [[INGREDIENT_TYPE_FILLING, 'salad', 50.0], [INGREDIENT_TYPE_SAUCE, 'ketchup', 60.5]])
    def test_set_ingredient_type_name_price(self, type, name, price):
        ingredient = Ingredient(type, name, price)

        assert ingredient.type == type
        assert ingredient.name == name
        assert ingredient.price == price

    @pytest.mark.parametrize('type, name, price', [[INGREDIENT_TYPE_FILLING, 'salad', 50.0], [INGREDIENT_TYPE_SAUCE, 'ketchup', 60.5]])
    def test_get_ingredient_type_returns_type(self, type, name, price):
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_type() == type

    @pytest.mark.parametrize('type, name, price', [[INGREDIENT_TYPE_FILLING, 'salad', 50.0], [INGREDIENT_TYPE_SAUCE, 'ketchup', 60.5]])
    def test_get_ingredient_name_returns_name(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('type, name, price', [[INGREDIENT_TYPE_FILLING, 'salad', 50.0], [INGREDIENT_TYPE_SAUCE, 'ketchup', 60.5]])
    def test_get_ingredient_price_returns_price(self, type, name, price):
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_price() == price
