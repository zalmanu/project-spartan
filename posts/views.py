from django.shortcuts import render
from django.shortcuts import redirect
from models import Announcement
from categories.models import Category
from bidding.models import Offer
from .forms import PostForm, BiddingForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from .models import EditPostForm


@login_required
def create_post(request):
    curruser = request.user
    errors = []
    form = PostForm(request.POST)
    if request.method == 'POST':
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
    return render(request, 'posts/create_post.html', {
        'cod': curruser.account.code,
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

        form = BiddingForm(request.POST)
        if form.is_valid():
            price = form.cleaned_data['price']
            kind = form.cleaned_data['kind']
            if price > post.money:
                errors.append(
                    'You offer more than the employer is willing to pay')
            elif price < 0:
                errors.append('Invalid offer')
            else:
                offer = Offer.objects.create(price=price, kind=kind,
                                             spartan=request.user.spartan,
                                             post=post)
                offer.save()
                confirms.append('Offer was sent')
        else:
            errors.append('Form is not valid')
    form = BiddingForm()
    return render(request, 'posts/post.html', {
        'cod': request.user.account.code,
        'post': post,
        'form': form,
        'errors': errors,
        'confirms': confirms
    })


def edit_post(request, slug):
    post = get_object_or_404(Announcement, slug=slug, status=False)
    if post.author != request.user:
        return HttpResponseForbidden()
    form = EditPostForm(data=request.POST or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/post/' + post.slug)
    return render(request, 'posts/edit_post.html', {
        'cod': request.user.account.code,
        'post': post,
        'form': form,
    })
