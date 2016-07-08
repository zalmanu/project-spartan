from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from forms import User_Edit, Account_Edit


@login_required
def profile(request):
    current_user = request.user
    user_form = User_Edit(data=request.POST or None,
                          instance=current_user, user=current_user)
    account_form = Account_Edit(data=request.POST or None,
                                instance=current_user.account)
    if request.method == 'POST':
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            current_user.account.code = current_user.account.gravatar_photo()
            current_user.account.save()
            return redirect('/profile')
    return render(request, 'profiles/profile.html', {
        'cod': current_user.account.code,
        'form': user_form,
        'form_acc': account_form
    })
