from django.shortcuts import render
from models import CreateReportForm
from django.contrib.auth.decorators import login_required


@login_required
def report(request):
    confirms = []
    curruser = request.user
    form = CreateReportForm(data=request.POST or None, user=curruser)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = curruser
            form.save()
            confirms.append("The report was sent")
    return render(request, 'report/report.html', {
        'cod': curruser.account.code,
        'form': form,
        'confirm': confirms
    })
