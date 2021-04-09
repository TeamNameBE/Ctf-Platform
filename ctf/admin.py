from django.contrib import admin

import ctf.models as models


# Register your models here.
class CTFAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "website")
    ordering = ("id", "name")
    search_fields = ("name",)


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("name", "points", "validated")
    ordering = ("id", "name")
    search_fields = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("id", "name")
    search_fields = ("name",)


class ChallengeFileAdmin(admin.ModelAdmin):
    list_display = ("file",)
    ordering = ("id",)


admin.site.register(models.CTF, CTFAdmin)
admin.site.register(models.Challenge, ChallengeAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.ChallengeFile, ChallengeFileAdmin)
