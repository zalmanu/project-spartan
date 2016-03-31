from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from useractions.models import Announcement


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        post_text = request.POST.get('text')
        adress = request.POST.get('adress')
        country = request.POST.get('country')
        city = request.POST.get('city')
        category = request.POST.get('category')
        time = request.POST.get('timepicker-one')
        announcement = Announcement.objects.create(title=title, text=post_text, address=adress, country=country,
                                                   city=city, timePost=time, author=request.user)
        announcement.save()
    return render(request, 'useractions/create_post.html')


def profile(request):
    return render(request, 'useractions/profile.html')


def category(request):
    return render(request, 'useractions/garden.html')
