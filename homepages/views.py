from django.shortcuts import render, render_to_response
from posts.models import Announcement, Category


def home(request):
    categories = Category.objects.all()
    if request.user.is_authenticated():
        curruser = request.user
        return render_to_response('homepages/home.html', {
            'ann': Announcement.objects.filter(status = False).order_by('-creation_date')[:5],
            'categories': categories,
            'user': curruser,
            'cod': curruser.account.cod})
    else:
        return render(request, 'homepages/index.html', {
            'categories': categories
        })
