import json

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from models import Room, Message
from forms import SendMessageForm

messages = []

def create_json(room):
    for msg in room.messages.all():
        message_details = {
            'message': msg.message,
            'sent': msg.submitter
        }
        messages.append(message_details)

        
@login_required
def room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    if request.method == "POST":
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            Message.objects.create(room = room, message=message, submitter=request.user)
            create_json(room)
            return render(request, 'chat/room.html', {
                'room': room,
                'messages': json.dumps(messages),
            })
        else:
            form = SendMessageForm()
            return render(request, 'chat/room.html', {
                'room': room,
                'messages': json.dumps(messages),
                'error': ['Invalid message'],
                'form' : form
            })
    else:
        form = SendMessageForm()
        return render(request, 'chat/room.html', {
            'room': room,
            'messages': json.dumps(messages),
            'form' : form
        })
    
def rooms(request):
    user = request.user
    return render(request, 'chat/rooms.html', {
            'rooms': user.rooms })
