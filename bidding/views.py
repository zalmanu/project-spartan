import json
import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from posts.models import Announcement
from bidding.models import Oferta
from chat.models import Room
from review.models import UrlUnique


@csrf_exempt
def posts(request):
    if request.method == 'POST':
        context = {"result": "success"}
        if request.POST.get('oferta'):
            oferta_id = request.POST.get('oferta')
            oferta = Oferta.objects.get(id=oferta_id)
            oferta.post.spartan = oferta.spartan
            oferta.post.pret = oferta.pret
            oferta.post.status = True
            oferta.status = True
            oferta.save()
            oferta.post.save()
            new_room = Room.objects.create(spartan=oferta.post.spartan.user,
                                           employer=oferta.post.author,
                                           post=oferta.post)
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
                   'cod': request.user.account.cod}
        if request.user.account.has_related_object():
            context['bids'] = request.user.spartan.licitari.all()
        return render(request, 'bidding/myPosts.html', context)
