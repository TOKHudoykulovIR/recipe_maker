from django.contrib import admin, messages
from .models import Recipe, RecipeIngredient
from . import views

admin.site.register(RecipeIngredient)


class RecipeIngredients(admin.StackedInline):
    model = RecipeIngredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredients, ]
    actions = ['convert_to_pdf', ]

    @admin.action(description='Convert to Pdf')
    def convert_to_pdf(self, request, queryset):
        if len(queryset) > 1:
            self.message_user(request, "You can convert one file at a time", messages.WARNING)
        else:
            recipe_ingredients = RecipeIngredient.objects.filter(recipe=queryset[0])
            context_dict = {
                "recipe": queryset[0],
                "ingredients": recipe_ingredients
            }
            return views.render_to_pdf('app/pdf_template.html', context_dict)


admin.site.register(Recipe, RecipeAdmin)
