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
            announcement = Announcement.objects.create(title=title, text=post_text, address=adress, country=country,
                                                       category=category, city=city, timePost=time, author=request.user)
            announcement.save()


            subject='Anunt Project Spartan'
            messagetip="Ati postat un anunt cu Titlul : %s ,\n Text: %s \n Adress: %s \n Country : %s \nCity: %s \n category: %s \n Time : %s \n O zi buna!"  %(title,post_text,adress,country,city,category,time)
            from_email=settings.EMAIL_HOST_USER
            send_mail(subject, messagetip, from_email,
            [request.user.email], fail_silently=True)
            return redirect('/')
        if request.user.is_active and not  request.user.is_superuser:
             return render(request, 'useractions/create_post.html', {
             'cod': curruser.account.cod})
        else:return render(request, 'useractions/create_post.html', {
            'cod': 1})
    else:
        return redirect('/login/')


def profile(request):
    if request.user.is_authenticated():
        curruser = request.user
        if request.method == 'POST':
            if request.POST.get('username') is not None:
                username = request.POST.get('username')
                curruser.username = username
                curruser.save()
                if request.user.is_active and not  request.user.is_superuser:
                    return render(request, 'useractions/profile.html', {
                    'cod': curruser.account.cod})
                else:return render(request, 'useractions/profile.html', {
                    'cod': 1})

        else:
              if request.user.is_active and not  request.user.is_superuser:
                    return render(request, 'useractions/profile.html', {
                        'cod': curruser.account.cod})
              else:
                  return render(request, 'useractions/profile.html', {'cod': 1})
    else:
        return redirect('/login/')


def category(request):
    if request.user.is_authenticated:
        curruser = request.user
        if request.user.is_active and not  request.user.is_superuser:
            return render(request, 'useractions/category.html', {
            'categories': ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others'],
            #'kind': kind
            'cod': curruser.account.cod
             })
        else: return render(request, 'useractions/category.html', {
            'categories': ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others'],
            #'kind': kind
            'cod': 1
             })
    else:
        return redirect('/')
