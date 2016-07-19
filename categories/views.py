import json

from django.template import RequestContext
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from models import Category
from posts.models import Announcement


@login_required
def category(request, kind):
    categories = Category.objects.all()
    page_category = get_object_or_404(Category, name=kind)
    return render(request, 'category/category.html', {
        'categories': categories,
        'kind': page_category,
        'anns': Announcement.objects.filter(category=page_category,
                                            status=False),
    },
                  context_instance=RequestContext(request))


@login_required
@csrf_exempt
def filter(request):
    category = request.POST.get("category")
    if request.POST.get("maxprice") or request.POST.get("minprice"):
        if request.POST.get("maxprice"):
            price = request.POST.get("maxprice")
            price = int(price)
            posts_category = get_object_or_404(Category, name=category)
            posts = Announcement.objects.filter(category=posts_category,
                                                money__lte=price)
        else:
            price = request.POST.get("minprice")
            price = int(price)
            posts_category = get_object_or_404(Category, name=category)
            posts = Announcement.objects.filter(category=posts_category,
                                                money__gte=price)
        results = {'posts': []}
        array = results.get('posts')
        for post in posts:
            post_details = {
                'title': post.title,
                'description': post.description,
                'slug': post.get_absolute_url(),
                'image': post.image.url
            }
            array.append(post_details)
        return HttpResponse(json.dumps(results))
    return HttpResponseForbidden
