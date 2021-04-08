from django.contrib import admin

import ctf.models as models


# Register your models here.
class CTFAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "website")
    ordering = ("id", "name")
    search_fields = ("name", )


admin.site.register(models.CTF, CTFAdmin)
