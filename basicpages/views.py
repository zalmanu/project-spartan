from django.shortcuts import render, render_to_response
from useractions.models import Announcement


def home(request):
    if request.user.is_authenticated():
        return render_to_response('useractions/home.html', {
            'ann' : Announcement.objects.all().order_by('-creation_date')[:3]
           })
    else:
        return render(request, 'basicpages/index.html')
            
