from django.contrib import admin
from useractions.models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']
    ordering = ['creation_date']
    
admin.site.register(Announcement, AnnouncementAdmin)




