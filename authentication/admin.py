from django.contrib import admin
from authentication.models import Spartan

# Register your models here.
class SpartanAdmin(admin.ModelAdmin):
   list_display = ['nume', 'prenume']
   ordering = ['prenume']

admin.site.register(Spartan,SpartanAdmin)
