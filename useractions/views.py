from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from useractions.models import Announcement
from categories.models import Category
from authentication.models import Account
from spartan.models import Spartan
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .forms import ProfileEditForm, PostForm
import md5
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


@login_required
def create_post(request):
    curruser = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            post_text = form.cleaned_data['text']
            adress = form.cleaned_data['adress']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            category = form.cleaned_data['category']
            time = form.cleaned_data['timePost']
            time = ":".join(map(lambda item: item.strip(), time.split(":")))
            data_post = form.cleaned_data['data']
            money_user = form.cleaned_data['price']
            category_object = get_object_or_404(Category, name=category)
            announcement = Announcement.objects.create(title=title,
                                                       text=post_text,
                                                       address=adress,
                                                       country=country,
                                                       money=money_user,
                                                       city=city,
                                                       data=data_post,
                                                       timePost=time,
                                                       author=request.user,
                                                       category=category_object)
            announcement.save()
            subject = 'Anunt Project Spartan'
            messagetip = " Buna % s , \n Ati postat un anunt cu succes! \n" \
                         " Titlul : %s ,\n Text: %s \n Adress: %s \n " \
                         "Country : %s \n City: %s \n category: %s \n" \
                         " Time : %s \n Data indepliniri task-ului: %s \n " \
                         "Suma maxima pentru licitatie: %s lei \n" \
                         " O zi buna!" % (
                             request.user.username, title, post_text, adress,
                             country, city, category, time, data_post,
                             money_user)
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, messagetip, from_email,
                      [request.user.email], fail_silently=True)
            posturl = announcement.get_absolute_url()
            return redirect(posturl)
        else:
            return render(request, 'useractions/create_post.html', {
                'cod': curruser.account.cod,
                'form': form,
                'errors': ['Invalid form']})
    else:
        form = PostForm
        if request.user.is_active and not request.user.is_superuser:
            return render(request, 'useractions/create_post.html', {
                'cod': curruser.account.cod,
                'form': form})
        else:
            return render(request, 'useractions/create_post.html', {
                'cod': '61e1380365703a4c73c2480673d8993b',
                'form': form})


@login_required
def profile(request):
    curruser = request.user
    form = ProfileEditForm
    if request.method == 'POST':

        if request.user.is_active and not request.user.is_superuser:
            return render(request, 'useractions/profile.html', {
                'cod': curruser.account.cod,
                'form': form
            })

        else:
            return render(request, 'useractions/profile.html', {
                'cod': 1,
                'form': form})

    else:
        if request.user.is_active and not request.user.is_superuser:
            return render(request, 'useractions/profile.html', {
                'cod': curruser.account.cod,
                'form': form, })
        else:
            return render(request, 'useractions/profile.html', {
                'cod': '61e1380365703a4c73c2480673d8993b',
                'form': form})


def profileGeneral(request):
    return render(request, 'useractions/profilegeneral.html')


