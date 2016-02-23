from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def profile(request):
    if request.user.is_authenticated():
        return render(request, 'useractions/home.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))
