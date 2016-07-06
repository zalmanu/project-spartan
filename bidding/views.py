import json
import random
from django.http import HttpResponse
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
        if request.POST.get('offer'):
            offer_id = request.POST.get('offer')
            offer = Offer.objects.get(id=offer_id)
            offer.post.spartan = offer.spartan
            offer.post.price = offer.price
            offer.post.status = True
            offer.status = True
            offer.save()
            offer.post.save()
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
        context = {'posts': request.user.posts.all(),
                   'cod': request.user.account.code}
        if request.user.account.has_related_object():
            context['bids'] = request.user.spartan.bids.all()
        return render(request, 'bidding/myPosts.html', context)
