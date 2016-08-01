# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.

import json
from datetime import datetime
from cgi import escape

from django.template import RequestContext
from django.http import HttpResponseForbidden, HttpResponse
from django.core.paginator import Paginator
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from models import Category
from authentication.models import City
from posts.models import Announcement


@login_required
def category(request, kind):
    categories = Category.objects.all()
    page_category = get_object_or_404(Category, name=kind)
    anns = Announcement.objects.all().filter(category=page_category,
                                             status=False).order_by(
                                                 '-id')
    page = request.GET.get('page')
    paginator = Paginator(anns, 8)
    return render(request, 'category/category.html', {
        'categories': categories,
        'kind': page_category,
        'anns': paginator.page(page),
        'num_pages': paginator.num_pages,
        'page_number': page
    },
                  context_instance=RequestContext(request))


@login_required
@csrf_exempt
def filter(request):
    category = request.POST.get("category")
    posts_category = get_object_or_404(Category, name=category)
    if (
        request.POST.get("maxprice") or request.POST.get("minprice") or
        request.POST.get("date") or request.POST.get("city")
    ):
        if request.POST.get("maxprice"):
            price = request.POST.get("maxprice")
            price = int(price)
            posts = Announcement.objects.filter(category=posts_category,
                                                money__lte=price,
                                                status=False)
        elif request.POST.get("minprice"):
            price = request.POST.get("minprice")
            price = int(price)
            posts = Announcement.objects.filter(category=posts_category,
                                                money__gte=price,
                                                status=False)
        elif request.POST.get("date"):
            data = request.POST.get("date")
            data = datetime.strptime(data,
                                     "%m/%d/%Y")
            posts = Announcement.objects.filter(category=posts_category,
                                                data__range=[timezone.now(),
                                                             data],
                                                status=False)
        elif request.POST.get("city"):
            city = request.POST.get("city")
            city = City.objects.get(name=city)
            posts = Announcement.objects.filter(category=posts_category,
                                                city=city, status=False)
        results = {'posts': []}
        array = results.get('posts')
        for post in posts:
            if(post.image):
                post_image = post.image.url
            else:
                post_image = "/static/img/thumbnails/picjumbo.com_IMG_3241.jpg"
            print post_image
            post_details = {
                'title': escape(post.title),
                'description': escape(post.description),
                'slug': post.get_absolute_url(),
                'image': escape(post_image)
            }
            array.append(post_details)
        return HttpResponse(json.dumps(results))
    return HttpResponseForbidden
