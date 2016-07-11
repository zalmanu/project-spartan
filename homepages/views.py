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

from django.shortcuts import render, render_to_response
from posts.models import Announcement, Category


def home(request):
    categories = Category.objects.all()
    if request.user.is_authenticated():
        current_user = request.user
        return render_to_response('homepages/home.html', {
            'ann': Announcement.objects.filter(status=False).order_by(
                '-creation_date')[:5],
            'categories': categories,
            'user': current_user,
            'cod': current_user.account.code})
    else:
        return render(request, 'homepages/index.html', {
            'categories': categories
        })
