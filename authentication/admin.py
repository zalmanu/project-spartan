from django.contrib import admin
from authentication.models import Spartan, Account

# Register your models here.
class SpartanAdmin(admin.ModelAdmin):
   list_display = ['nume', 'prenume']
   ordering = ['prenume']

class AccountAdmin(admin.ModelAdmin):
   list_distplay = ['user']
   ordering = ['user']

admin.site.register(Account, AccountAdmin)
admin.site.register(Spartan,SpartanAdmin)
