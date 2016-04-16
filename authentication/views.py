from django.shortcuts import render
from .forms import LoginForm, RegisterForm
import authentication.models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
import md5


def register_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                password2 = form.cleaned_data['password2']
                email = form.cleaned_data['email']
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
def reset_pass(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            u=request.user
            passwordold=request.POST.get('password')
            inf=request.user.check_password(passwordold)
            password1=request.POST.get('passwordnew')
            password2=request.POST.get('passwordnew1')
            if password1 ==password2 and inf==True:
                request.user.set_password(password1)
                u.save()
                return redirect('/')
            else:return render(request, "authentication/resetpass.html",{'errors': ['Incorrect  password']})
        else :
             return render(request, "authentication/resetpass.html")
    else : 
        return redirect('/login/')
