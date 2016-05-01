from django.contrib import admin
from models import Spartan


class SpartanAdmin(admin.ModelAdmin):
    list_display = ['nume', 'prenume']
    ordering = ['prenume']


admin.site.register(Spartan, SpartanAdmin)
