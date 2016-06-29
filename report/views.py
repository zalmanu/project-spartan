from django.shortcuts import render
from models import Report, CreateReportForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def report(request):
    errors = []
    confirms = []
    curruser = request.user
    form = ReportForm(request.POST)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user = User.objects.get(username=username)
                if curruser.username == username:
                    errors.append("This username  is your username")
                else:
                    status = form.cleaned_data['statut']
                    if status == 'Employer':
                        text = form.cleaned_data['text']
                        report = Report.objects.create(username=username,
                                                       status=status,
                                                       text=text,
                                                       author=curruser)
                        report.save()
                        confirms.append("The report was sent")
                    else:
                        if user.account.has_related_object():
                            text = form.cleaned_data['text']
                            report = Report.objects.create(username=username,
                                                           status=status,
                                                           text=text,
                                                           author=curruser)
                            report.save()
                            confirms.append("The report was sent")
                        else:
                            errors.append("This user is not a spartan")
            except User.DoesNotExist:
                errors.append("This user does not exist")

        else:
            errors.append("Invalid form")
    return render(request, 'report/report.html', {
        'cod': curruser.account.code,
        'form': form,
        'confirm': confirms,
        'errors': errors})
