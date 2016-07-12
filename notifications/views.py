import json

from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse

from .models import Notification


@csrf_exempt
def seen(request):
    if request.method == "POST":
        if request.POST.get('notif'):
            context = {"result": "success"}
            notif_id = request.POST.get("notif")
            print notif_id
            notification = Notification.get_object_or_404(pk=notif_id)
            notification.seen = True
            notification.save()
            return HttpResponse(json.dumps(context),
                                content_type='application/json')
    return HttpResponseForbidden()
