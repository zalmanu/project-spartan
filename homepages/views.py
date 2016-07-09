from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

from haystack.forms import SearchForm

from posts.models import Announcement, Category


def home(request):
    categories = Category.objects.all()
    if request.user.is_authenticated():
        current_user = request.user
        form = SearchForm(request.GET)
        posts = None
        if form.data != {} and form.is_valid():
            posts = form.search()
            return render_to_response('search/search.html', {
                'posts': posts,
                'form': form
            })
        return render_to_response('homepages/home.html', {
            'ann': Announcement.objects.filter(status=False).order_by(
                '-creation_date')[:4],
            'categories': categories,
            'user': current_user,
            'cod': current_user.account.code,
            'form': form
        })
    else:
        return render(request, 'homepages/index.html', {
            'categories': categories
        })


@login_required
def search_posts(request):
    posts = None
    form = SearchForm(request.GET)
    if form.data != {} and form.is_valid():
        posts = form.search()
    return render_to_response('search/search.html', {
        'posts': posts,
        'form': form
    })
