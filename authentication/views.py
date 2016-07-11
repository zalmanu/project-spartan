# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.

from django.shortcuts import render
from .forms import LoginForm, PasswordResetForm
from .forms import UserRegisterForm, AccountRegisterForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def register_page(request):
    form = UserRegisterForm(data=request.POST or None)
    acc_form = AccountRegisterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and acc_form.is_valid():
            form.instance.set_password(form.cleaned_data['password'])
            form.save()
            acc_form.instance.user = form.instance
            acc_form.save()
            acc_form.instance.code = acc_form.instance.gravatar_photo()
            acc_form.save()
            user = authenticate(username=form.instance.username,
                                password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
    return render(request, "authentication/register.html", {
                'form': form,
                'acc_form': acc_form
        })


def login_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        errors = []
        form = LoginForm(request.POST)
        if request.method == 'POST':
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
        return render(request, "authentication/logIn.html", {
            'form': form,
            'errors': errors})


@login_required
def reset_pass(request):
    errors = []
    form = PasswordResetForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            password_old = form.cleaned_data['old_password']
            password_new = form.cleaned_data['password_1']
            check = password_new == form.cleaned_data['password_2']
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
    return render(request, "authentication/resetpass.html",
                  {'form': form,
                   'cod': request.user.account.code,
                   'errors': errors})


def forgot(request):
    return render(request, 'authentication/forget.html')


def forgotnewpass(request):
    if request.method == 'POST':
        return render(request, 'authentication/forget.html')
    else:
        return render(request, 'authentication/newpass.html')
