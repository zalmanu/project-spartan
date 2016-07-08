from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from models import Room
from .forms import CreateMessageForm


@login_required
def room(request, slug):
    chat_room = get_object_or_404(Room, slug=slug)
    form = CreateMessageForm(data=request.POST or None)
    if chat_room.spartan != request.user and \
       chat_room.employer != request.user:
        return HttpResponseForbidden()
    if chat_room.employer == request.user:
        other = chat_room.spartan
    else:
        other = chat_room.employer
    if request.method == "POST":
        if form.is_valid():
            form.instance.room = chat_room
            form.instance.submitter = request.user
            form.save()
    return render(request, 'chat/chat.html', {
        'chat_room': chat_room,
        'messages': chat_room.messages.all(),
        'form': form,
        'other': other,
        'cod': request.user.account.code
    })


@login_required
def rooms(request):
    user = request.user
    spartan_messages = user.spa_rooms
    employer_messages = user.empl_rooms
    context = {'spa_messages': spartan_messages.all(),
               'empl_messages': employer_messages.all(),
               'cod': user.account.code}
    return render(request, 'chat/rooms.html', context)
