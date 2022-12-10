from django.core.validators import RegexValidator
from django.db import models
from ckeditor.fields import RichTextField


# recipes model
class Recipe(models.Model):
    name = models.CharField(max_length=180)
    section = models.CharField(max_length=100)
    method = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


# recipe ingredients model
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients")
    ingredient = models.CharField(max_length=140)
    unit = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


# blanks model
class Blank(models.Model):
    client = models.CharField(max_length=60, blank=True, null=True)
    client_contact = models.CharField(max_length=80, blank=True, null=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    client_phone = models.CharField(validators=[phoneNumberRegex], max_length=16, blank=True, null=True)
    client_email = models.EmailField(blank=True, null=True)

    venue = models.CharField(max_length=50, blank=True, null=True)
    venue_contact = models.CharField(max_length=80, blank=True, null=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    venue_phone = models.CharField(validators=[phoneNumberRegex], max_length=16, blank=True, null=True)
    venue_email = models.EmailField(blank=True, null=True)

    event_manager = models.CharField(max_length=60)
    event_type_dinner_etc = models.CharField(max_length=100, blank=True, null=True)
    event_planner = models.CharField(max_length=60)
    guest_num = models.PositiveIntegerField(blank=True, null=True)

    food_leaves = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    chefs_leave = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    porters_leave = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    total_waiters = models.PositiveIntegerField(blank=True, null=True)
    dietaries = RichTextField(blank=True, null=True)

    food_arrives = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    chefs_arrives = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    porter_arrives = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    total_chefs = models.PositiveIntegerField(blank=True, null=True)
    menu = RichTextField(blank=True, null=True)

    staff_food = models.CharField(max_length=100, blank=True, null=True)
    drinks_garnishes = models.CharField(max_length=100, blank=True, null=True)
    drugget_and_tape = models.CharField(max_length=100, blank=True, null=True)


# blank metas model
class BlankMeta(models.Model):
    blank = models.ForeignKey(Blank, on_delete=models.CASCADE)
    timings = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    action = models.CharField(max_length=120, blank=True, null=True)


# furniture_row_header = (("t", "TABLES"), ("tl", "TABLE LINEN"), ("n", "NAPKINS"), ("d", "DISPOSABLE NAPKINS"))

# furniture model
class Furniture(models.Model):
    blank = models.ForeignKey(Blank, on_delete=models.CASCADE)
    equipment = models.CharField(blank=True, editable=True, max_length=20)
    quantity = models.IntegerField(blank=True, null=True)
    supplied_by = models.CharField(max_length=70, blank=True, null=True)
    location_purpose = models.CharField(max_length=70, blank=True, null=True)
