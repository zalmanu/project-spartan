import md5

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from forms import ProfileEditForm

@login_required
def profile(request):
    curruser = request.user
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
            if form.cleaned_data['email'] is not None:
                email  = form.cleaned_data['email']
                if User.objects.filter(email=email).exists():
                    return render(request, "profiles/profile.html", {
                        'form': form,
                        'errors': ["Email is already taken"]})
                else:
                    curruser.email = email
                    curruser.save()
                    usshash = md5.new()
                    usshash.update(email)
                    cod=usshash.hexdigest()
                    curruser.account.cod = cod
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
            if request.user.is_active and not request.user.is_superuser:
                return render(request, 'profiles/profile.html', {
                    'cod': curruser.account.cod,
                    'form': form
                })
                
            else:
                return render(request, 'profiles/profile.html', {
                    'cod': 1,
                    'form': form})
        else :
            return render(request, "authentication/register.html", {
                        'form': form,
                        'errors': ["Invalid form"]})
    else:
        form = ProfileEditForm()
        if request.user.is_active and not request.user.is_superuser:
            return render(request, 'profiles/profile.html', {
                'cod': curruser.account.cod,
                'form': form, })
        else:
            return render(request, 'profiles/profile.html', {
                'cod': '61e1380365703a4c73c2480673d8993b',
                'form': form})


