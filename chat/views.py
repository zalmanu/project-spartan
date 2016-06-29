from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from models import Room, CreateMessageForm


@login_required
def room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    form = CreateMessageForm(data=request.POST or None)
    if room.spartan != request.user and room.employer != request.user:
        return HttpResponseForbidden()
    if room.employer == request.user:
        other = room.spartan
    else:
        other = room.employer
    if request.method == "POST":
        if form.is_valid():
            form.instance.room = room
            form.instance.submitter = request.user
            form.save()
    return render(request, 'chat/chat.html', {
        'room': room,
        'messages': room.messages.all(),
        'form': form,
        'other': other,
        'cod': request.user.account.code
    })


def rooms(request):
    user = request.user
    spa_messages = user.spa_rooms
    empl_messages = user.empl_rooms
    context = {'spa_messages': spa_messages.all(),
               'empl_messages': empl_messages.all(),
               'cod': user.account.code}
    return render(request, 'chat/rooms.html', context)
