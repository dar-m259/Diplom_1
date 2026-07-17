import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    
    def test_database_has_initial_data(self):
        database = Database()

        assert hasattr(database, 'buns')
        assert hasattr(database, 'ingredients')

        assert isinstance(database.buns, list)
        assert isinstance(database.ingredients, list)

        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

    @pytest.mark.parametrize('name, price', [["black bun", 100], ["white bun", 200], ["red bun", 300]])
    def test_database_bun_names_and_prices_are_correct(self, name, price):
        database = Database()

        bun_exists = any(bun.name == name and bun.price == price for bun in database.buns)
        
        assert bun_exists

    @pytest.mark.parametrize('type, name, price', [
        [INGREDIENT_TYPE_SAUCE, "hot sauce", 100], [INGREDIENT_TYPE_SAUCE, "sour cream", 200], [INGREDIENT_TYPE_SAUCE, "chili sauce", 300], 
        [INGREDIENT_TYPE_FILLING, "cutlet", 100], [INGREDIENT_TYPE_FILLING, "dinosaur", 200], [INGREDIENT_TYPE_FILLING, "sausage", 300]])
    def test_database_ingredient_types_names_and_prices_are_correct(self, type, name, price):
        database = Database()

        ingredient_exists = any(ingredient.type == type and ingredient.name == name and ingredient.price == price for ingredient in database.ingredients)

        assert ingredient_exists

    def test_database_available_buns_returns_buns_list(self):
        database = Database()
        
        assert database.available_buns() == database.buns

    def test_database_available_ingredients_returns_ingredients_list(self):
        database = Database()

        assert database.available_ingredients() == database.ingredients
