from django.contrib import admin
from authentication.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['user']
    ordering = ['user']


admin.site.register(Account, AccountAdmin)
