from django.contrib import admin
from .models import Recipe

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "cocktail_type",
        "spirit_types",
        "instructions",
        "ingredients",
        "image",
    )
    list_filter = ("cocktail_type",)

admin.site.register(Recipe, RecipeAdmin)    