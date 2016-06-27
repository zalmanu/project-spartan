from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from models import Announcement
from bidding.models import Offer
from .forms import BiddingForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from .models import EditPostForm, CreatePostForm


@login_required
def create_post(request):
    curruser = request.user
    form = CreatePostForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = curruser
            form.save()
            form.instance.creation_email(curruser)
            return redirect(form.instance.get_absolute_url())
    return render(request, 'posts/create_post.html', {
        'cod': curruser.account.code,
        'form': form})


@login_required
def post(request, slug):
    post = get_object_or_404(Announcement, slug=slug)
    if post.status and request.user != post.author and \
       request.user != post.spartan.user:
        raise Http404()
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
