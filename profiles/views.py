from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from forms import ProfileEditForm

@login_required
def profile(request):
    curruser = request.user
    form = ProfileEditForm
    if request.method == 'POST':

        if request.user.is_active and not request.user.is_superuser:
            return render(request, 'profiles/profile.html', {
                'cod': curruser.account.cod,
                'form': form
            })

        else:
            return render(request, 'profiles/profile.html', {
                'cod': 1,
                'form': form})

    else:
        if request.user.is_active and not request.user.is_superuser:
            return render(request, 'profiles/profile.html', {
                'cod': curruser.account.cod,
                'form': form, })
        else:
            return render(request, 'profiles/profile.html', {
                'cod': '61e1380365703a4c73c2480673d8993b',
                'form': form})


