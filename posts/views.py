from django.shortcuts import render
from django.shortcuts import redirect
from models import Announcement
from categories.models import Category
from bidding.models import Oferta
from .forms import PostForm, LicitatieForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def create_post(request):
    curruser = request.user
    errors = []
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            post_text = form.cleaned_data['text']
            adress = form.cleaned_data['adress']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            category = form.cleaned_data['category']
            time = form.cleaned_data['timePost']
            time = ":".join(map(lambda item: item.strip(), time.split(":")))
            data_post = form.cleaned_data['data']
            money_user = form.cleaned_data['price']
            category_object = get_object_or_404(Category, name=category)
            announcement = Announcement.objects.create(title=title,
                                                       text=post_text,
                                                       address=adress,
                                                       country=country,
                                                       money=money_user,
                                                       city=city,
                                                       data=data_post,
                                                       timePost=time,
                                                       author=request.user,
                                                       category=category_object
                                                       )
            announcement.save()
            announcement.creation_email(curruser)
            posturl = announcement.get_absolute_url()
            return redirect(posturl)
        else:
            errors.append('Invalid form')

    form = PostForm
    return render(request, 'posts/create_post.html', {
        'cod': curruser.account.cod,
        'form': form,
        'errors': errors})


@login_required
def post(request, slug):
    post = get_object_or_404(Announcement, slug=slug, status=False)
    errors = []
    confirms = []

    if request.method == 'POST':
        if request.POST.get("deletePost"):
            post.delete()
            return redirect('/')

        form = LicitatieForm(request.POST)
        if form.is_valid():
            pret = form.cleaned_data['pret']
            tip = form.cleaned_data['tip']
            if pret > post.money:
                errors.append(
                    'You offer more than the employer is willing to pay')
            elif pret < 0:
                errors.append('Invalid offer')
            else:
                oferta = Oferta.objects.create(pret=pret, tip=tip,
                                               spartan=request.user.spartan,
                                               post=post)
                oferta.save()
                confirms.append('Oferta a fost trimisa')
        else:
            errors.append('Form is not valid')
    form = LicitatieForm()
    return render(request, 'posts/post.html', {
        'cod': request.user.account.cod,
        'post': post,
        'form': form,
        'errors': errors,
        'confirms': confirms
    })
