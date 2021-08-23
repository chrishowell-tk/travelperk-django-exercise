from django.test import TestCase
from core import models


class ModelTests(TestCase):

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            name='Cucumber'
        )
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            name='Chicken Tikka Masala',
            description='Chicken Tikka pieces in a succulent Masala sauce'
        )
        self.assertEqual(str(recipe), recipe.name)
