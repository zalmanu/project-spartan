from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

def create_post(request):
    if request.method == 'POST':
        title = request.POST('title')
        post_text = request.POST('text')
        adress = request.POST('adress')
        country = request.POST('country')
        city = request.POST('city')
        category = request.POST('category')
        
        
    return render(request, 'useractions/create_post.html')

def category(request, category_id):
    return render(request, 'useractions/garden.html')
