from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from useractions.models import Announcement
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
#            category = request.POST.get('category')
            time = request.POST.get('timepicker-one')
            announcement = Announcement.objects.create(title=title, text=post_text, address=adress, country=country,
                                                       city=city, timePost=time, author=request.user)
            print announcement
# category=category

            announcement.save()
        return render(request, 'useractions/create_post.html')
    else:
        return redirect('/login')


def profile(request):
    return render(request, 'useractions/profile.html')


def garden(request):
    return render(request, 'useractions/garden.html')


def transport(request):
    return render(request, 'useractions/transport.html')


def curatenie(request):
    return render(request, 'useractions/curatenie.html')


def baby(request):
    return render(request, 'useractions/baby.html')


def gatit(request):
    return render(request, 'useractions/gatit.html')


def altele(request):
    return render(request, 'useractions/altele.html')



