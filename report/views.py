from django.shortcuts import render
from models import Report
from .forms import ReportForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def report(request):
    errors = []
    confirms = []
    curruser = request.user
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if request.user.username == username:
                errors.append("This username  is your username")
            else:
                status = form.cleaned_data['statut']
                if status == 'Employer':
                    try:
                        User.objects.get(username=username)
                        text = form.cleaned_data['text']
                        report = Report.objects.create(username=username,
                                                       status=status,
                                                       text=text,
                                                       author=request.user)
                        report.save()
                        confirms.append("The report was sent")
                    except User.DoesNotExist:
                        errors.append("This employer doesn't exist")
                else:
                    try:
                        user = User.objects.get(username=username)
                        text = form.cleaned_data['text']
                        report = Report.objects.create(username=username,
                                                       status=status,
                                                       text=text,
                                                       author=request.user)
                        report.save()
                        confirms.append("The report was sent")
                    except (User.DoesNotExist or
                            not user.account.has_related_object()):
                        print user.username
                        errors.append("This user doesn't exist")

        else:
            errors.append("Invalid form")
    form = ReportForm
    return render(request, 'report/report.html', {
        'cod': curruser.account.code,
        'form': form,
        'confirm': confirms,
        'errors': errors})
