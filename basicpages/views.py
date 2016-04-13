from django.shortcuts import render, render_to_response
from useractions.models import Announcement


def home(request):
    if request.user.is_authenticated():
        curruser = request.user
        if request.user.is_active and not  request.user.is_superuser:
            print curruser.account.cod
            a=Announcement.objects.filter(category='Curatenie')
            return render_to_response('useractions/home.html', {
            'ann': a,#Announcement.objects.all().order_by('-creation_date')[:5],
                'categories': ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others'],
                'user': curruser,
                'cod': curruser.account.cod
                
           })
        else: return render_to_response('useractions/home.html', {
            'ann': Announcement.objects.all().order_by('-creation_date')[:5],
            'categories': ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others'],
            'user': curruser,
            'cod':  '61e1380365703a4c73c2480673d8993b'
           })
    else:
        return render(request, 'basicpages/index.html', {
            'categories': ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others']
        })
