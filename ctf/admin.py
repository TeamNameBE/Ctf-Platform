from django.contrib import admin

import ctf.models as models


@admin.register(models.CTF)
class CTFAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "website")
    ordering = ("id", "name")
    search_fields = ("name",)


@admin.register(models.Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("name", "points", "validated")
    ordering = ("id", "name")
    search_fields = ("name",)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("id", "name")
    search_fields = ("name",)
