from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from models import CreateReportForm


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
