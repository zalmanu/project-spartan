import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from authentication.models import Account,Spartan
from useractions.models import Announcement 
from .forms import LicitatieForm
from bidding.models import Oferta


@csrf_exempt
def posts(request):
    if request.method == 'POST':
        oferta_id = request.POST.get('oferta')
        oferta = Oferta.objects.get(id=oferta_id)
        oferta.post.spartan = oferta.spartan
        return HttpResponse(json.dumps({"result": "success"}), content_type='application/json')
    else:
        if request.user and not  request.user.is_superuser:
            return render(request, 'bidding/myPosts.html',{
                'posts': request.user.posts.all(),
                'cod': request.user.account.cod,
            })
        else:
            return render(request, 'bidding/myPosts.html',{
                'posts': request.user.posts.all(),
                'cod': '61e1380365703a4c73c2480673d8993b'
            })


@login_required
def post(request, slug):
    post = get_object_or_404(Announcement, slug = slug)
    if request.method == 'POST':
        form = LicitatieForm(request.POST)
        if form.is_valid():
            pret = form.cleaned_data['pret']
            tip = form.cleaned_data['tip']
            user = request.user
            form = LicitatieForm()
            if pret > post.money:
                return render(request,'bidding/post.html',{
                    'cod': request.user.account.cod,
                    'post': post,
                    'form': form,
                    'errors': ['Oferi mai mult de cat cel ce a pus anuntul este dispus sa plateasca']
                })
            else:
                oferta = Oferta.objects.create(pret = pret, tip = tip, spartan = request.user.spartan, post = post)
                oferta.save()
                return render(request,'bidding/post.html',{
                    'cod': request.user.account.cod,
                    'post': post,
                    'form': form,
                    'confirms': ['Oferta a fost trimisa']
                })
        else :
            return render(request,'bidding/post.html',{
                'cod': request.user.account.cod,
                'post': post,
                'form': form,
                'errors': ['Form is not valid']
            })
    else:
        form = LicitatieForm()
        if request.user and not request.user.is_superuser:
            return render(request,'bidding/post.html',{
                'cod': request.user.account.cod,
                'post': post,
                'form': form
            })
        else:
            print "what"
            return render(request, 'bidding/myPosts.html',{
                'cod': '61e1380365703a4c73c2480673d8993b',
                'post': post,
                'form': form
            })

