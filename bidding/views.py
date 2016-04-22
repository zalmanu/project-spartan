from django.shortcuts import render



def myPost(request):
    return render(request, 'bidding/myPosts.html')

def post(request):
    return render(request,'bidding/post.html')

def yourPost(request):
    return render(request,'bidding/yourPost.html')