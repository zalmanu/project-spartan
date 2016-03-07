from django.shortcuts import render, render_to_response
from useractions.models import Announcement


def home(request):
    if request.user.is_authenticated():
        return render(request, 'useractions/home.html')
    else:
        return render_to_response('basicpages/index.html', {
            'ann' : Announcement.objects.all().order_by('-creation_date')[:3]
            })
