from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from useractions.models import Announcement
from authentication.models import Account
from django.contrib import messages
from django.contrib.auth.models import User
# from django.conf import settings
# from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ProfileEditForm
import md5

import datetime



def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def create_post(request):
    if request.user.is_authenticated():
        curruser = request.user
        if request.method == 'POST':
            title = request.POST.get('title')
            post_text = request.POST.get('text')
            adress = request.POST.get('adress')
            country = request.POST.get('country')
            city = request.POST.get('city')
            category = request.POST.get('category')
            time = request.POST.get('timepicker-one')
            time = ":".join(map(lambda item: item.strip(), time.split(":")))
            data_post=request.POST.get('Date')
            money_user=request.POST.get('money')
            announcement = Announcement.objects.create(title=title, text=post_text, address=adress, country=country,
                                                       category=category,money =money_user, city=city,data=data_post, timePost=time, author=request.user)
            announcement.save()


            subject='Anunt Project Spartan'
            messagetip=" Buna % s , \n Ati postat un anunt cu succes! \n" \
                       " Titlul : %s ,\n Text: %s \n Adress: %s \n Country : %s \n City: %s \n category: %s \n" \
                       " Time : %s \n Data indepliniri task-ului: %s \n " \
                       "Suma maxima pentru licitatie: %s lei \n O zi buna!"  %(request.user.username,title,post_text,adress,country,city,category,time,data_post,money_user)
            from_email=settings.EMAIL_HOST_USER
            send_mail(subject, messagetip, from_email,
            [request.user.email], fail_silently=True)
            return redirect('/')
        if request.user.is_active and not  request.user.is_superuser:
             return render(request, 'useractions/create_post.html', {
             'cod': curruser.account.cod})
        else:return render(request, 'useractions/create_post.html', {
            'cod': '61e1380365703a4c73c2480673d8993b'})
    else:
        return redirect('/login/')


def profile(request):
    if request.user.is_authenticated():
        curruser = request.user
        now = datetime.datetime.now()
        if request.method == 'POST':
            if request.POST.get('username'):
                username = request.POST.get('username')
                curruser.username = username
            if request.POST.get('email'):
                email = request.POST.get('email')
                curruser.email = email
                usshash = md5.new()
                usshash.update(email)
                curruser.account.cod = usshash.hexdigest()
            if request.POST.get('country'):
                country = request.POST.get('country')
                curruser.account.country = country
            if request.POST.get('city'):
                city = request.POST.get('city')
                curruser.account.city = city
            if request.POST.get('phone'):
                phone = request.POST.get('phone')
                curruser.account.phone = phone
            curruser.account.save()
            curruser.save()

            # subject='test'
            # email_post=request.POST.get('email')
            # messages_post=request.POST.get('message')
            # from_email=settings.EMAIL_HOST_USER
            # send_mail(subject, messages_post, from_email,
            # [request.user.email], fail_silently=True)


            if request.user.is_active and not  request.user.is_superuser:
                    return render(request, 'useractions/profile.html', {
                    'cod': curruser.account.cod,
                    'time':now,
                    })
               
            else:
                return render(request, 'useractions/profile.html', { 'time':now,
                    'cod': 1})

        else:
            if request.user.is_active and not  request.user.is_superuser:
                    return render(request, 'useractions/profile.html', {
                        'cod': curruser.account.cod,
                        'form': ProfileEditForm, 'time':now, })
            else:
                  return render(request, 'useractions/profile.html',{
                         'cod': '61e1380365703a4c73c2480673d8993b',
                         'form': ProfileEditForm, 'time':now,})
    else:
        return redirect('/login/')


def category(request, kind):
    if request.user.is_authenticated:
        curruser = request.user
        if request.user.is_active and not  request.user.is_superuser:
            return render(request, 'useractions/category.html', {
            'categories': ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others'],
            'kind': kind,
            'cod': curruser.account.cod
             })
        else: return render(request, 'useractions/category.html', {
            'categories': ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others'],
            'kind': kind,
            'cod': '61e1380365703a4c73c2480673d8993b'
             })
    else:
        return redirect('/')
