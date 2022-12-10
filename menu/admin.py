from django.contrib import admin, messages
from .models import Recipe, RecipeIngredient, Blank, BlankMeta, Furniture
from . import views
# from django.forms import BaseInlineFormSet


# ----- RECIPE INLINE MODULE -----
class RecipeIngredients(admin.StackedInline):
    model = RecipeIngredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredients, ]
    actions = ['convert_menu_to_pdf', ]

    @admin.action(description='Convert to pdf')
    def convert_menu_to_pdf(self, request, queryset):
        if len(queryset) > 1:
            self.message_user(request, "You can convert one file at a time", messages.WARNING)
        else:
            recipe_ingredients = RecipeIngredient.objects.filter(recipe=queryset[0])
            context_dict = {
                "recipe": queryset[0],
                "ingredients": recipe_ingredients
            }
            return views.render_to_pdf('app/menu_template.html', context_dict)


admin.site.register(Recipe, RecipeAdmin)
# ----- / -----


# ----- BLANK INLINE MODULE -----
class BlankMetasInline(admin.StackedInline):
    model = BlankMeta
    extra = 0


# class FurnitureInlineFormset(BaseInlineFormSet):
#     def __init__(self, *args, **kwargs):
#         kwargs['initial'] = [
#             {"equipment": "t"},
#             {"equipment": "tl"},
#             {"equipment": "n"},
#             {"equipment": "d"},
#         ]
#         super(FurnitureInlineFormset, self).__init__(*args, **kwargs)


class FurnitureInline(admin.StackedInline):
    readonly_fields = ("equipment", )
    fields = ("equipment", "quantity", "supplied_by", "location_purpose")
    model = Furniture
    extra = 4
    max_num = 4
    # formset = FurnitureInlineFormset


class BlankAdmin(admin.ModelAdmin):
    inlines = [BlankMetasInline, FurnitureInline]
    actions = ['convert_event_sheet_to_pdf', ]
    fields = (("client", "client_contact", "client_phone", "client_email"),
              ("venue", "venue_contact", "venue_phone", "venue_email"),
              ("event_manager", "event_type_dinner_etc", "event_planner", "guest_num"),
              ("food_leaves", "chefs_leave"), ("porters_leave", "total_waiters"), "dietaries",
              ("food_arrives", "chefs_arrives"), ("porter_arrives", "total_chefs"), "menu",
              ("staff_food", "drinks_garnishes"), "drugget_and_tape")

    @admin.action(description='Convert to pdf ')
    def convert_event_sheet_to_pdf(self, request, queryset):
        if len(queryset) > 1:
            self.message_user(request, "You can convert one file at a time", messages.WARNING)
        else:
            event_meta = BlankMeta.objects.filter(blank=queryset[0])
            context_dict = {
                "event_data": queryset[0],
                "event_meta": event_meta
            }
            return views.render_to_pdf('app/event_sheet_template.html', context_dict)


admin.site.register(Blank, BlankAdmin)
# ----- / -----
