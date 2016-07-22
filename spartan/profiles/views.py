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

from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from forms import User_Edit, Account_Edit


@login_required
def profile(request):
    current_user = request.user
    user_form = User_Edit(data=request.POST or None,
                          instance=current_user, user=current_user)
    account_form = Account_Edit(request.POST or None,
                                request.FILES or None,
                                instance=current_user.account)
    if request.method == 'POST':
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            current_user.account.save()
            return redirect('/profile')
    return render(request, 'profiles/profile.html', {
        'form': user_form,
        'form_acc': account_form
    },
                  context_instance=RequestContext(request))
