# Copyright 2015-2016 Emanuel Covaci, Fineas Silaghi, Sebastian Males
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

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from models import Announcement
from bidding.forms import CreateOfferForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from .forms import EditPostForm, CreatePostForm


@login_required
def create_post(request):
    current_user = request.user
    form = CreatePostForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = current_user
            form.save()
            form.instance.creation_email(current_user)
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
        if request.POST.get("deletePost") and post.author == request.user:
            post.delete()
            return redirect('/')
        if form.is_valid():
            form.instance.post = post
            form.instance.spartan = request.user.spartan
            form.save()
            confirms.append('Offer was sent')
    return render(request, 'posts/post.html', {
        'cod': request.user.account.code,
        'post': post,
        'form': form,
        'confirms': confirms
    })


@login_required
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
