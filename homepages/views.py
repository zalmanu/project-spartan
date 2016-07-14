from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

from posts.models import Announcement, Category


def home(request):
    categories = Category.objects.all()
    if request.user.is_authenticated():
        current_user = request.user
        return render_to_response('homepages/home.html', {
            'ann': Announcement.objects.filter(status=False).order_by(
                '-creation_date')[:4],
            'categories': categories,
            'user': current_user,
            'cod': current_user.account.code
        })
    else:
        return render(request, 'homepages/index.html', {
            'categories': categories
        })
