from django.shortcuts import render
from django.contrib.auth.models import User
from authentication.models import Account,Spartan

def myPost(request):
    return render(request, 'bidding/myPosts.html',)

def post(request):
    return render(request,'bidding/post.html')

def yourPost(request):
     if request.user.is_active and not  request.user.is_superuser:
            return render(request, 'bidding/yourPost.html', {
                'cod': request.user.account.cod,
                })
     else:
            return render(request, 'useractions/profile.html',{
                'cod': '61e1380365703a4c73c2480673d8993b',})