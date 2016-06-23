from django.contrib import admin
from models import Spartan


class SpartanAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']
    ordering = ['first_name']


admin.site.register(Spartan, SpartanAdmin)
