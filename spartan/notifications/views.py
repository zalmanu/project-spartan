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

import json

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Notification


@login_required
@csrf_exempt
def seen(request):
    if request.method == "POST":
        if request.POST.get('notif'):
            notif_id = request.POST.get("notif")
            print notif_id
            notification = Notification.objects.get(id_hash=notif_id,
                                                    receiver=request.user)
            if notification.seen or notification.receiver != request.user:
                return HttpResponseForbidden()
            notification.seen = True
            notification.save()
            context = {"result": "success",
                       "type": notification.not_type}
            return HttpResponse(json.dumps(context),
                                content_type='application/json')
    return HttpResponseForbidden()


@login_required
@csrf_exempt
def notification_delete(request):
    if request.method == "POST":
        if request.POST.get("id"):
            notif_id = request.POST.get("id")
            notification = Notification.objects.get(id_hash=notif_id)
            if request.user != notification.receiver:
                return HttpResponseForbidden()
            notification.delete()
            return HttpResponse(json.dumps({'result': 'succes'}),
                                content_type='application/json')
    return HttpResponseForbidden()


def notification_page(request):
    return render_to_response('notifications/notifications-page.html',context_instance=RequestContext(request))
