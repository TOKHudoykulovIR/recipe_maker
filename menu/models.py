from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=180)
    section = models.CharField(max_length=100)
    method = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients")
    ingredient = models.CharField(max_length=140)
    unit = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)