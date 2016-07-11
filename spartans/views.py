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

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from models import Spartan
from .forms import CreateSpartanForm


@login_required
def spartan(request):
    confirm = []
    form = CreateSpartanForm(data=request.POST or None, user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            form.instance.activation_email()
            confirm.append('You\'ve completed the form, '
                           'wait for admin\'s confirmation')
    return render(request, 'spartan/spartan.html', {
        'cod': request.user.account.code,
        'form': form,
        'confirms': confirm})


@login_required
def user(request, slug):
    current_spartan = get_object_or_404(Spartan, slug=slug)
    return render(request, 'spartan/SpartanPage.html', {
        'reviews': current_spartan.reviews,
        'spartan': current_spartan,
        'img_spartan': current_spartan.user.account.code,
        'cod': request.user.account.code,
    })
