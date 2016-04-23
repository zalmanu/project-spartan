from django.contrib import admin
from useractions.models import Announcement, Category

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']
    ordering = ['creation_date']

    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

    
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Category, CategoryAdmin)



