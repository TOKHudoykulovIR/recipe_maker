# Generated by Django 4.1.3 on 2022-12-10 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0002_alter_recipe_method"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe",
            old_name="date",
            new_name="created",
        ),
    ]
