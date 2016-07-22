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

from .forms import CreateReportForm


@login_required
def report(request):
    confirms = []
    current_user = request.user
    form = CreateReportForm(data=request.POST or None, user=current_user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = current_user
            form.save()
            confirms.append("The report was sent")
    return render(request, 'report/report.html', {
        'form': form,
        'confirm': confirms
    },
                  context_instance=RequestContext(request))
