from django.shortcuts import render
from models import CreateReportForm
from django.contrib.auth.decorators import login_required


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
        'cod': current_user.account.code,
        'form': form,
        'confirm': confirms
    })
