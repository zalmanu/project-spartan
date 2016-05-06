import md5

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from authentication.models import Account
from forms import ProfileEditForm
from models import User_Edit, Account_Edit

@login_required
def profile(request):
    curruser = request.user
    errors = []
    user_form = User_Edit(data=request.POST or None, instance = curruser, user=curruser)
    account_form = Account_Edit(data=request.POST or None, instance = curruser.account)
    if request.method == 'POST':
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            return redirect('/profile')
    return render(request, 'profiles/profile.html', {
        'cod': curruser.account.cod,
        'form': user_form,
        'form_acc': account_form
    })
