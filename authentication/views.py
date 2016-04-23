from django.shortcuts import render
from .forms import LoginForm, RegisterForm, PasswordResetForm, ForgotPasswordForm
import authentication.models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
import md5
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.urlresolvers import reverse


def register_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                if User.objects.filter(username=username).exists():
                    return render(request, "authentication/register.html", {
                     'form':form,
                     'errors':["Username is already taken"]})
                password = form.cleaned_data['password']
                password2 = form.cleaned_data['password2']
                email = form.cleaned_data['email']
                if User.objects.filter(email=email).exists():
                    return render(request, "authentication/register.html", {
                     'form':form,
                     'errors':["Email is already taken"]})
                city = form.cleaned_data['city']
                country = form.cleaned_data['country']
                phone = form.cleaned_data['phone']
                if password == password2:
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
                    form = RegisterForm()
                    return render(request, "authentication/register.html", {
                     'form':form,
                     'errors':["Passwords do not match"]})

            else:
                form = RegisterForm()
                return render(request, "authentication/register.html", {
                     'form':form,
                     'errors':["Invalid form"]})
        else:
            form = RegisterForm()
            return render(request, "authentication/register.html", {
                 'form': form})


def login_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('/')
                
                else:
                    return render(request, "authentication/logIn.html", {
                        'errors': ['Incorrect username or password'],
                        'form': form
                    })
            else:
                return render(request, "authentication/logIn.html", {
                'errors': ['Invalid form'],
                'form': form
                })
        else:
            form = LoginForm()
            return render(request, "authentication/logIn.html",{
                'form': form
            })
        
@login_required
def reset_pass(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            password_old = form.cleaned_data['oldpass']
            password_new = form.cleaned_data['pass1']

            check = password_new == form.cleaned_data['pass2']
            if not check:
                return render(request, "authentication/resetpass.html",
                              {'errors': ['Those two password are not the same'],
                               'form': form})

            if request.user.check_password(password_old):
                request.user.set_password(password_new)
                request.user.save()
                user = authenticate(username=request.user.username,
                                    password=password_new)
                login(request, user)
            else:
                return render(request, "authentication/resetpass.html",
                              {'errors': ['Incorrect password'],
                               'form': form})

        else:
            return render(request, "authentication/resetpass.html",
                          {'errors': ['Invalid form'],
                           'form': form})
    else:
        form = PasswordResetForm
        return render(request, "authentication/resetpass.html", {'form': form})
    return redirect('/')

def forgotpassword(request):
    if request.method == 'POST':  
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_user = User.objects.filter(Q(email = email))
            print associated_user
            if associated_user.exists():
                return password_reset(request, template_name='authentication/forgotpassword.html',
                                      email_template_name='authentication/password_reset_email.html',
                                      post_reset_redirect=reverse('forgotpassword'))
            else:
                return render(request, 'authentication/forgotpassword.html',
                              {'form':form ,
                               'errors': ['There is no user associated with this email adress']})

    else:
        form = ForgotPasswordForm()
        return render(request, 'authentication/forgotpassword.html', {'form':form })


def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='forgotten.html',
        uidb36=uidb36, token=token, post_reset_redirect=reverse('success'))
