# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.
import json
import random
import string

from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404

from channels import Group
from haystack.forms import SearchForm

from .models import Announcement
from .forms import EditPostForm, CreatePostForm
from bidding.forms import CreateOfferForm
from .tasks import notify_spartans, email_user, notify_bid


@login_required
def create_post(request):
    current_user = request.user
    form = CreatePostForm(request.POST or None, request.FILES or None,
                          user=current_user)
    if request.method == 'POST':
        if form.is_valid():
            post = form.instance
            post.author = current_user
            form.save()
            category = post.category
            url = post.get_absolute_url()
            messagetip = " You successfully posted an announce!"
            email_user.delay(messagetip, current_user.username,
                             current_user.email,
                             "Spartan Tasks Post")
            id_hash = ''.join(random.choice(
                string.ascii_uppercase + string.digits) for _ in range(6))
            notify_spartans.delay(category.name, post.city,
                                  post.title,
                                  url, id_hash)
            html = """
            <a href=\"""" + url + """\" id="seen_notif_req"
            data-notification=\"""" + id_hash + """\"
            onmouseover="seen_not(this.getAttribute('data-notification'));">
            <li class="list-group-item" id=\"""" + id_hash + """\">
            <i class="fa fa-exclamation-circle icon"></i>New post in your area
            </li>
            </a>
            """
            dic = {
                'author': current_user.username,
                'html': html,
                'posts': 'post'
            }
            Group("spartans-" + category.name +
                  "-" + post.city).send({'text': json.dumps(dic)})
            return redirect(post.get_absolute_url())
    return render(request, 'posts/create_post.html', {
        'form': form}, context_instance=RequestContext(request))


@login_required
def post(request, slug):
    post = get_object_or_404(Announcement, slug=slug)
    if post.status and request.user != post.author and \
       request.user != post.spartan.user:
        raise Http404()
    form = CreateOfferForm(data=request.POST or None, post=post)
    other_posts = Announcement.objects.exclude(id=post.id).order_by('-id')[:4]
    average = 0
    confirms = []
    bids = post.offers.all().order_by('price')[:5]
    if request.method == 'POST':
        if request.POST.get("deletePost") and post.author == request.user:
            post.delete()
            return redirect('/')
        if form.is_valid():
            bid = form.instance
            bid.post = post
            bid.spartan = request.user.spartan
            form.save()
            receiver = post.author.username
            id_hash = ''.join(random.choice(
                string.ascii_uppercase + string.digits) for _ in range(6))
            html = """
            <a href=\"""" + post.get_absolute_url() + """\" id="seen_notif_req"
            data-notification=\"""" + id_hash + """\"
            onmouseover="seen_not(this.getAttribute('data-notification'));">
            <li class="list-group-item" id=\"""" + id_hash + """\">
            <i class="fa fa-exclamation-circle icon"></i>
            Someone bid on your post
            </li>
            </a>
            """
            dic = {
                'html': html,
                'author': bid.spartan.user.username,
                'type': 'bid'
            }
            Group("channel-" + receiver).send({
                'text': json.dumps(dic)})
            notify_bid.delay(receiver, post.get_absolute_url(),
                             bid.post.title, id_hash)
            confirms.append('Offer was sent')
    if post.offers.all():
        for bid in post.offers.all():
            average += bid.price
            print average
        average /= post.offers.count()
        print post.offers.count()
    return render(request, 'posts/post.html', {
        'post': post,
        'form': form,
        'other': other_posts,
        'confirms': confirms,
        'average': average,
        'post_bids': bids
    }, context_instance=RequestContext(request))


@login_required
def edit_post(request, slug):
    post = get_object_or_404(Announcement, slug=slug, status=False)
    if post.author != request.user:
        return HttpResponseForbidden()
    form = EditPostForm(request.POST or None, request.FILES or None,
                        instance=post, user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/post/' + post.slug)
    return render(request, 'posts/edit_post.html', {
        'post': post,
        'form': form,
    }, context_instance=RequestContext(request))


@login_required
def search(request):
    form = SearchForm(request.GET or None)
    posts = None
    if form.data != {} and form.is_valid():
        posts = form.search()
    return render_to_response('search/search.html', {
        'posts': posts
    }, context_instance=RequestContext(request))
