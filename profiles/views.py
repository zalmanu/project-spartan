import md5

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from authentication.models import Account
from forms import ProfileEditForm
from models import User_Edit

@login_required
def profile(request):
    curruser = request.user
    errors = []
    form = User_Edit(data=request.POST or None, instance = curruser, user=curruser)
    if request.method == 'POST':
        if form.is_valid():
            print "heh"
            form.save()
            return redirect('/')
    return render(request, 'profiles/profile.html', {
        'cod': curruser.account.cod,
        'form': form,
    })
