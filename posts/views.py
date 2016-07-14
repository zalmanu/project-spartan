import json

from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404

from channels import Group

from .models import Announcement, EditPostForm, CreatePostForm
from bidding.models import CreateOfferForm
from .tasks import notify_spartans, email_user


@login_required
def create_post(request):
    current_user = request.user
    form = CreatePostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.instance
            form.instance.author = current_user
            form.save()
            category = form.instance.category
            messagetip = " Hi! % s , \n You successfully"\
                         "posted an announce! \n" \
                         " Title: %s ,\n Description: %s \n Address: %s \n " \
                         "Country : %s \n City: %s \n Category: %s \n" \
                         " Time : %s \n Date: %s \n " \
                         "Highest bid price: %s eur \n" \
                         " Have a nice day! - Team Spartan" % (
                             current_user.username, post.title,  post.text,
                             post.address,
                             post.country,  post.city,  post.category.name,
                             post.timePost, post.data, post.money)
            email_user.delay(messagetip, current_user.email,
                             "Spartan Tasks Post")
            notify_spartans.delay(category.name, form.instance.city,
                                  form.instance.author.username)
            html = """
            <span class="subject">
            </span>
            <span class="message">
            A new post <b id="notification-bid">in your area</b>
            </span>
            </a>
            """
            dic = {
                'author': current_user.username,
                'html': html
            }
            Group("spartans-" + category.name +
                  "-" + form.instance.city).send({'text': json.dumps(dic)})
            return redirect(form.instance.get_absolute_url())
    return render(request, 'posts/create_post.html', {
        'cod': current_user.account.code,
        'form': form})


@login_required
def post(request, slug):
    post = get_object_or_404(Announcement, slug=slug)
    form = CreateOfferForm(data=request.POST or None, post=post)
    if post.status and request.user != post.author and \
       request.user != post.spartan.user:
        raise Http404()
    confirms = []
    if request.method == 'POST':
        if request.POST.get("deletePost"):
            post.delete()
            return redirect('/')
        if form.is_valid():
            form.instance.post = post
            form.instance.spartan = request.user.spartan
            form.save()
            confirms.append('Offer was sent')
    return render(request, 'posts/post.html', {
        'ann': Announcement.objects.filter(status=False).order_by(
            '-creation_date')[:4],
        'user': request.user,
        'cod': request.user.account.code,
        'post': post,
        'form': form,
        'confirms': confirms
    })


def edit_post(request, slug):
    post = get_object_or_404(Announcement, slug=slug, status=False)
    if post.author != request.user:
        return HttpResponseForbidden()
    form = EditPostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/post/' + post.slug)
    return render(request, 'posts/edit_post.html', {
        'cod': request.user.account.code,
        'post': post,
        'form': form,
    })

