from django.contrib import admin
from .models import Character

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    search_fields = ("name", "powers")
    list_filter = ("category",)
    ordering = ("name",)
