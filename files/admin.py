from django.contrib import admin
from files import models


@admin.register(models.ChallengeFile)
class ChallengeFileAdmin(admin.ModelAdmin):
    list_display = ("file",)
    ordering = ("id",)
