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

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from models import Category
from posts.models import Announcement


@login_required
def category(request, kind):
    categories = Category.objects.all()
    page_category = get_object_or_404(Category, name=kind)
    current_user = request.user
    return render(request, 'category/category.html', {
        'categories': categories,
        'kind': page_category,
        'cod': current_user.account.code,
        'ann': Announcement.objects.filter(category=page_category,
                                           status=False)
    })
