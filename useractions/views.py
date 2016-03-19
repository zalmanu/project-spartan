from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

def create_post(request):
    return render(request, 'useractions/create_post.html')

def category(request):
    return render(request, 'useractions/garden.html')
