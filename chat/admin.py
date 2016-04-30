from django.contrib import admin

from models import Room, Message

class RoomAdmin(admin.ModelAdmin):
    list_display = ['offer']
    ordering = ['offer']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['message']
    ordering = ['message']
    
admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
