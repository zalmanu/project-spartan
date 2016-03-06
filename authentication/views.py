from django.shortcuts import render
from authentication.models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        city = request.POST.get('city')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        photo = request.FILES.get('photo')
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        account = Account.objects.create(user=new_user, city=city, country=country, telefon=phone)
        account.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    else:
        return render(request, "authentication/register.html")


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        else:
            messages.error(request, 'Numele de utilizator sau parola nu corespund')
            return render(request, "authentication/logIn.html")
    return render(request, "authentication/logIn.html")
