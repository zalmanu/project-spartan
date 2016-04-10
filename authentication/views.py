from django.shortcuts import render
import authentication.models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages


def register_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            city = request.POST.get('city')
            country = request.POST.get('country')
            phone = request.POST.get('phone')
            new_user = User.objects.create_user(username, email, password)
            new_user.save()
            account = authentication.models.Account.objects.create(user=new_user, city=city, country=country, telefon=phone)
            account.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, "authentication/register.html")


def login_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
            else:
                print username
                messages.error(request, 'Incorrect username or password')
                return render(request, "authentication/logIn.html")
        return render(request, "authentication/logIn.html")
