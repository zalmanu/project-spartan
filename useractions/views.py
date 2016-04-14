from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from useractions.models import Announcement
from authentication.models import Account,Spartan
from django.contrib import messages
from django.contrib.auth.models import User
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
            data_post=datetime.datetime.strptime(data_post, '%m/%d/%Y').strftime('%Y-%m-%d')
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
        an = Announcement.objects.filter(category=kind)
        curruser = request.user
        if request.user.is_active and not  request.user.is_superuser:
            return render(request, 'useractions/category.html', {
            'categories': ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others'],
            'kind': kind,
            'cod': curruser.account.cod,
            'ann': an
             })
        else: return render(request, 'useractions/category.html', {
            'categories': ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others'],
            'kind': kind,
           'cod': '61e1380365703a4c73c2480673d8993b',
            'ann': an
             })
    else:
        return redirect('/')

def sartan(request):
    if request.user.is_authenticated():
        curruser = request.user
        if request.method == 'POST':
            nume=request.POST.get('nume')
            prenume=request.POST.get('prenume')
            data_nasterii=request.POST.get('Data_nasteri')
            adress=request.POST.get('adress')
            cnp=request.POST.get('CNP')
            serie=request.POST.get('serie')
            cui=request.POST.get('cui')
            contBancar=request.POST.get('contBancar')
            abilitate1=request.POST.get('abilitate1')
            abilitate2=request.POST.get('abilitate2')
            abilitate3=request.POST.get('abilitate3')
            spartan =Spartan.objects.create(nume=nume, prenume=prenume, data_nasterii=data_nasterii,
                                            address=adress, cnp=cnp,serie=serie,cui=cui,
                                            contBancar=contBancar,
                                             abilitate1=abilitate1,abilitate2=abilitate2,
                                             abilitate3=abilitate3,
                                            author=request.user)
            spartan.save()
            return render(request, 'useractions/spartan.html' ,{'errors': ['Ati completat cu succes formularul,asteptati confirmarea administratorului!']})
            # return redirect('/')
        # if request.user.is_active and not  request.user.is_superuser:
        #      return render(request, 'useractions/spartan.html', {
        #      'cod': curruser.account.cod})
        #  else:
        return render(request, 'useractions/spartan.html')
    else:
        return redirect('/login/')


         # return render(request, "useractions/spartan.html")
