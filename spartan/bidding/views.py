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
import random

from django.http import HttpResponse, HttpResponseForbidden
from django.template import RequestContext
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from posts.models import Announcement
from bidding.models import Offer
from chat.models import Room
from review.models import UrlUnique


@login_required
@csrf_exempt
def posts(request):
    if request.method == 'POST':
        context = {"result": "success"}
        if(
            request.POST.get('offer') or request.POST.get('post') or
                request.POST.get('post_empl')
        ):
            if request.POST.get('offer'):
                offer_id = request.POST.get('offer')
                offer = Offer.objects.get(id=offer_id)
                offer.post.spartan = offer.spartan
                offer.post.price = offer.price
                offer.post.status = True
                offer.status = True
                offer.save()
                offer.post.save()
                objects_to_keep = Offer.objects.filter(id=offer.id)
                Offer.objects.filter(post=offer.post).exclude(
                    pk__in=objects_to_keep).delete()
                new_room = Room.objects.create(spartan=offer.post.spartan.user,
                                               employer=offer.post.author,
                                               post=offer.post)
                new_room.save()
            elif request.POST.get('post'):
                post_id = request.POST.get('post')
                post = Announcement.objects.get(id=post_id)
                post.spartan_done = True
                post.save()
            elif request.POST.get('post_empl'):
                post_id = request.POST.get('post_empl')
                post = Announcement.objects.get(id=post_id)
                post.room.delete()
                slug = post.spartan.slug
                post.spartan.tasks += 1
                post.spartan.save()
                post.delete()
                context['slug'] = slug
                uhash = random.getrandbits(32)
                UrlUnique.objects.create(un_hash=uhash)
                context['hash'] = uhash
            return HttpResponse(json.dumps(context),
                                content_type='application/json')
        else:
            return HttpResponseForbidden
    else:
        cont = {'posts': request.user.posts.all()}
        if request.user.account.has_related_object():
            cont['bids'] = request.user.spartan.bids.all()
        return render(request, 'bidding/myPosts.html', cont,
                      context_instance=RequestContext(request))
