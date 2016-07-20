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
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from .models import Spartan
from forms import CreateSpartanForm
from posts.tasks import email_user


@login_required
def spartan(request):
    cuser = request.user
    if cuser.account.has_related_object() and cuser.spartan.spartanStatus:
        raise PermissionDenied
    confirm = []
    form = CreateSpartanForm(data=request.POST or None)
    if request.method == 'POST':
        if not request.user.account.has_related_object() and form.is_valid():
            form.instance.user = request.user
            form.save()
            new_spartan = form.instance
            email_message = " Hi! % s , \n You submitted the form" \
                            " for becoming a spartan!\n" \
                            " Last name : %s ,\n First name : %s \n" \
                            "Birthday: %s \n" \
                            " Address : %s \n CNP: %s \n Serie: %s \n" \
                            " CUI : %s \n Bank account: %s \n " \
                            "Ability: %s \n  An admin will respond soon. " \
                            " - Team Spartan" % (
                                new_spartan.user.username,
                                new_spartan.last_name,
                                new_spartan.first_name,
                                new_spartan.birthday, new_spartan.address,
                                new_spartan.cnp, new_spartan.series,
                                new_spartan.cui,
                                new_spartan.bank, new_spartan.category.name)
            email_user.delay(email_message, request.user.email,
                             "Spartan activation")
            confirm.append('You\'ve completed the form, '
                           'wait for admin\'s confirmation')
    return render(request, 'spartan/spartan.html', {
        'form': form,
        'confirms': confirm,
        },
                  context_instance=RequestContext(request))


@login_required
def user(request, slug):
    current_spartan = get_object_or_404(Spartan, slug=slug)
    return render(request, 'spartan/SpartanPage.html', {
        'reviews': current_spartan.reviews,
        'spartan': current_spartan,
        'img_spartan': current_spartan.user.account.profile_image,
    },
                  context_instance=RequestContext(request))
