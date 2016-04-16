from django.shortcuts import render
import authentication.models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
import md5
from django.contrib.auth.decorators import login_required


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
            usshash = md5.new()
            usshash.update(new_user.email)
            account = authentication.models.Account.objects.create(user=new_user, city=city, country=country, telefon=phone, cod=usshash.hexdigest())
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
                return render(request, "authentication/logIn.html", {
                    'errors': ['Incorrect username or password']})
        else:
            return render(request, "authentication/logIn.html")


@login_required
def reset_pass(request):
    if request.method == 'POST':
        password_old = request.POST.get('password')
        password_new = request.POST.get('passwordnew')

        check = password_new == request.POST.get('passwordnew1')
        if not check:
            return render(request, "authentication/resetpass.html",
                          {'errors': ['Those two password are not the same']})

        if request.user.check_password(password_old):
            request.user.set_password(password_new)
            request.user.save()
            user = authenticate(username=request.user.username,
                                password=password_new)
            login(request, user)
        else:
            return render(request, "authentication/resetpass.html",
                          {'errors': ['Incorrect password']})

    else:
        return render(request, "authentication/resetpass.html")
    return redirect('/')