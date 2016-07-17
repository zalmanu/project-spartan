from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['seen']

admin.site.register(Notification, NotificationAdmin)
