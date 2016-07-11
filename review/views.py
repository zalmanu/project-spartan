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
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from .models import UrlUnique
from .forms import CreateReviewForm
from authentication.models import Spartan


@login_required
def review(request, slug, url_hash):
    form = CreateReviewForm(data=request.POST or None)
    if request.method == 'POST':
        if request.POST.get('dontp'):
            return redirect('/')
        if form.is_valid():
            url = get_object_or_404(UrlUnique, un_hash=url_hash, expired=False)
            url.expired = True
            url.save()
            form.instance.receiver = get_object_or_404(Spartan, slug=slug)
            form.instance.submitter = request.user
            form.save()
            current_spartan = form.instance.receiver
            current_spartan.rating += 1
            current_spartan.save()
            return redirect('/')
    return render(request, 'review/review.html',
                  {
                    'cod': request.user.account.code,
                    'form': form, 'slug': slug
                  })
