import pytest

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock

@pytest.fixture
def burger_with_ingredients():
    burger = Burger()
    burger.add_ingredient(Mock(type=INGREDIENT_TYPE_FILLING, name='salad', price=50.0, get_price=lambda: 50.0, get_name=lambda: 'salad', get_type=lambda: INGREDIENT_TYPE_FILLING)) #get_name=lambda: 'salad'
    burger.add_ingredient(Mock(type=INGREDIENT_TYPE_SAUCE, name='ketchup', price=60.5, get_price=lambda: 60.5, get_name=lambda: 'ketchup', get_type=lambda: INGREDIENT_TYPE_SAUCE)) #get_name=lambda: 'ketchup'
    burger.add_ingredient(Mock(type=INGREDIENT_TYPE_FILLING, name='cutlet', price=200.5, get_price=lambda: 200.5, get_name=lambda: 'cutlet', get_type=lambda: INGREDIENT_TYPE_FILLING)) #get_name=lambda: 'cutlet'

    return burger

@pytest.fixture
def burger_with_bun_and_ingredients(burger_with_ingredients):
    burger_with_ingredients.set_buns(Mock(name='cosmos bun', price=100.5, get_price=lambda: 100.5, get_name=lambda: 'cosmos bun')) #get_name=lambda: 'cosmos bun'
    
    return burger_with_ingredients
