from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from authentication.models import Account,Spartan
from useractions.models import Announcement 

def posts(request):

    if request.user and not  request.user.is_superuser:
           return render(request, 'bidding/myPosts.html',{
               'posts': request.user.posts.all(),
               'cod': request.user.account.cod
           })
    else:
        return render(request, 'bidding/myPosts.html',{
            'posts': request.user.posts.all(),
            'cod': '61e1380365703a4c73c2480673d8993b'
        })

def post(request, slug):
    post = get_object_or_404(Announcement, slug = slug)
    if request.user and not request.user.is_superuser:
        return render(request,'bidding/post.html',{
            'cod': request.user.account.cod,
            'post': post
        })
    else:
        return render(request, 'bidding/myPosts.html',{
            'cod': '61e1380365703a4c73c2480673d8993b',
            'post': post
        })

def yourPost(request):
     if request.user.is_active and not  request.user.is_superuser:
            return render(request, 'bidding/yourPost.html', {
                'cod': request.user.account.cod,
                })
     else:
            return render(request, 'useractions/profile.html',{
                'cod': '61e1380365703a4c73c2480673d8993b',})
