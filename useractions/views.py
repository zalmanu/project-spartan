from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from useractions.models import Announcement
from authentication.models import Account
from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def create_post(request):
    if request.user.is_authenticated():
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
            return redirect('/')
        return render(request, 'useractions/create_post.html')
    else:
        return redirect('/login/')


def profile(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            user = request.user
            acc = user.Account
            if request.POST.get('username') is not None:
                username = request.POST.get('username')
                user.username = username
                user.save()
                return redirect('/profile/')
            if request.POST.get('email') is not None:
                email = request.POST.get('email')
                user.email = email
                user.save()
                return redirect('/profile/')
        else:
             
             return render(request, 'useractions/profile.html',{"cod":user.Account.codeimg()})
    else:
        return redirect('/login/')

def category(request):
    if request.user.is_authenticated:
        return render(request, 'useractions/cateogory.html', {
            'categories' : ['Garden', 'Moving','Cleaning', 'Babysitting', 'Cooking', 'Others'],
        })
    else:
        return redirect('/')
