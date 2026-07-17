import pytest

from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from helpers import count_ingredients_price, get_ingredients_names


class TestBurger:
    
    def test_burger_empty_at_start(self):
        burger = Burger()

        assert burger.bun == None
        assert burger.ingredients == []

    def test_burger_set_buns_bun_is_set(self):
        mock_bun = Mock()
        mock_bun.configure_mock(name='cosmos bun', price=100.5)

        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_burger_add_ingredients_ingredient_added(self):
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(type= INGREDIENT_TYPE_SAUCE, name='ketchup', price = 60.5)

        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]

    @pytest.mark.parametrize('index', [0, 1, 2])
    def test_burger_remove_ingredients_removed(self, burger_with_ingredients, index):
        ingredient_to_remove = burger_with_ingredients.ingredients[index]
        new_list_len = len(burger_with_ingredients.ingredients) - 1

        burger_with_ingredients.remove_ingredient(index)

        assert len(burger_with_ingredients.ingredients) == new_list_len
        assert not ingredient_to_remove in burger_with_ingredients.ingredients

    @pytest.mark.parametrize('old_index, new_index', [[0, 1], [1, 2], [2, 1]])
    def test_burger_move_ingredient_moved(self, burger_with_ingredients, old_index, new_index):
        ingredient_to_move = burger_with_ingredients.ingredients[old_index]

        burger_with_ingredients.move_ingredient(old_index, new_index)
        new_list = burger_with_ingredients.ingredients

        assert new_list.index(ingredient_to_move) == new_index

    def test_burger_get_price_is_correct(self, burger_with_bun_and_ingredients):
        ingredients_price = count_ingredients_price(burger_with_bun_and_ingredients.ingredients)
        bun_price = burger_with_bun_and_ingredients.bun.price

        burger_price = bun_price * 2 + ingredients_price

        assert burger_with_bun_and_ingredients.get_price() == burger_price

    def test_burger_get_receipt_showed_correctly(self, burger_with_bun_and_ingredients):
        bun_name_top = [f'(==== {burger_with_bun_and_ingredients.bun.get_name()} ====)']

        ingredients_names_and_types = get_ingredients_names(burger_with_bun_and_ingredients.ingredients)
        
        bun_name_bottom = [f'(==== {burger_with_bun_and_ingredients.bun.get_name()} ====)\n']
        burger_price = [f'Price: {burger_with_bun_and_ingredients.get_price()}']
        
        receipt = bun_name_top + ingredients_names_and_types + bun_name_bottom + burger_price

        assert burger_with_bun_and_ingredients.get_receipt() == '\n'.join(receipt)
