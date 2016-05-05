from django.shortcuts import render
from .forms import LoginForm, RegisterForm, PasswordResetForm
import authentication.models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
import md5


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def register_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        errors = []
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                if User.objects.filter(username=username).exists():
                    errors.append("Username is already taken")
                password = form.cleaned_data['password']
                password2 = form.cleaned_data['password2']
                email = form.cleaned_data['email']
                if User.objects.filter(email=email).exists():
                    errors.append("Email is already taken")
                city = form.cleaned_data['city']
                country = form.cleaned_data['country']
                phone = form.cleaned_data['phone']
                if password.isdigit():
                    errors.append("Password is entirely numeric")
                if password != password2:
                    errors.append("Passwords do not match")
                if len(password) < 8:
                    errors.append("Password is too short")
                if errors:
                    form = RegisterForm()
                    return render(request, "authentication/register.html", {
                        'form': form,
                        'errors': errors})
                new_user = User.objects.create_user(username, email, password)
                new_user.save()
                account = authentication.models.Account.objects.create(
                    user=new_user, city=city, country=country,
                    telefon=phone)
                account.cod = account.gravatar_photo()
                account.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('/')
            else:
                errors.append("Invalid form")
    form = RegisterForm()
    return render(request, "authentication/register.html", {
                'form': form,
                'errors': errors})


def login_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        errors = []
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('/')

                else:
                    errors.append('Incorrect username or password')

            else:
                errors.append('Invalid form')
        form = LoginForm()
        return render(request, "authentication/logIn.html", {
            'form': form,
            'errors': errors})


@login_required
def reset_pass(request):
    errors = []
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            password_old = form.cleaned_data['oldpass']
            password_new = form.cleaned_data['pass1']
            check = password_new == form.cleaned_data['pass2']
            if not check:
                errors.append('Those two password are not the same')
            elif request.user.check_password(password_old):
                request.user.set_password(password_new)
                request.user.save()
                user = authenticate(username=request.user.username,
                                    password=password_new)
                login(request, user)
                return redirect('/')
            else:
                errors.append('Incorrect old password')
        else:
            errors.append('Invalid form')
    form = PasswordResetForm
    return render(request, "authentication/resetpass.html",
                  {'form': form,
                   'cod': request.user.account.cod,
                   'errors': errors})


def forgot(request):
    return render(request, 'authentication/forget.html')


def forgotnewpass(request):
    if request.method == 'POST':
        return render(request, 'authentication/forget.html')
    else:
        return render(request, 'authentication/newpass.html')
