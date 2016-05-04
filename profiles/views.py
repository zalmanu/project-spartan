import md5

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from forms import ProfileEditForm

@login_required
def profile(request):
    curruser = request.user
    errors = []
    if request.method == 'POST':
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['username'] != '':
                username = form.cleaned_data['username']
                if User.objects.filter(username=username).exists():
                    return render(request, "profiles/profile.html", {
                        'form': form,
                        'errors': ["Username is already taken"]})
                else:
                    curruser.username = username
                    curruser.save()
            if form.cleaned_data['email']!= '':
                email  = form.cleaned_data['email']
                if User.objects.filter(email=email).exists():
                    return render(request, "profiles/profile.html", {
                        'form': form,
                        'errors': ["Email is already taken"]})
                else:
                    curruser.email = email
                    curruser.save()
                    curruser.account.cod = curruser.account.gravatar_photo()
                    curruser.account.save()
            if form.cleaned_data['city'] is not None:
                city = form.cleaned_data['city']
                curruser.account.city = city
                curruser.account.save()
            if form.cleaned_data['country'] is not None:
                country = form.cleaned_data['country']
                curruser.account.country = country
                curruser.account.save()
            if form.cleaned_data['telefon'] is not None:
                telefon = form.cleaned_data['telefon']
                curruser.account.telefon = telefon
                curruser.account.save()
            form = ProfileEditForm()
        else :
            errors.append("Invalid form")
    form = ProfileEditForm()
    return render(request, 'profiles/profile.html', {
        'cod': curruser.account.cod,
        'form': form, 
        'errors': errors
    })
