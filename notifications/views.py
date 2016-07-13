import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse

from .models import Notification


@csrf_exempt
def seen(request):
    if request.method == "POST":
        if request.POST.get('notif'):
            context = {"result": "success"}
            notif_id = request.POST.get("notif")
            notification = Notification.objects.get(id=notif_id)
            notification.seen = True
            notification.save()
            return HttpResponse(json.dumps(context),
                                content_type='application/json')
    return HttpResponseForbidden()
