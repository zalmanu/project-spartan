# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
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
        'messages': chat_room.messages.order_by('timestamp'),
        'form': form,
        'other': other,
    }, context_instance=RequestContext(request))
