from django.shortcuts import render
from models import Report
from .forms import ReportForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def report(request):
    curruser = request.user
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if request.user.username == username:
                return render(request, 'report/report.html', {
                    'cod': curruser.account.cod,
                    'form': form,
                    'errors': ["This username  is your username "]})
            status = form.cleaned_data['statut']
            if status == 'Employer':
                try:
                    user = User.objects.get(username=username)

                except User.DoesNotExist:
                    return render(request, 'report/report.html', {
                        'cod': curruser.account.cod,
                        'form': form,
                        'errors': ["This employer doesn't exist"]})
            else:
                try:
                    user = User.objects.get(username=username)
                    if not user.account.has_related_object():
                        return render(request, 'report/report.html', {
                            'cod': curruser.account.cod,
                            'form': form,
                            'errors': ["This spartan doesn't exist"]})
                except User.DoesNotExist:
                    return render(request, 'report/report.html', {
                        'cod': curruser.account.cod,
                        'form': form,
                        'errors': ["This spartan doesn't exist"]})
            text = form.cleaned_data['text']
            report = Report.objects.create(username=username,
                                           status=status,
                                           text=text,
                                           author=request.user,
                                           )
            report.save()
            return render(request, 'report/report.html', {
                'cod': curruser.account.cod,
                'form': form,
                'confirm': ['The report was sent!']})
        else:
            return render(request, 'report/report.html', {
                'cod': curruser.account.cod,
                'form': form,
                'errors': ['Invalid form']})
    else:
        form = ReportForm
        if request.user.is_active and not request.user.is_superuser:
            return render(request, 'report/report.html', {
                'cod': curruser.account.cod,
                'form': form})
        else:
            return render(request, 'report/report.html', {
                'cod': '61e1380365703a4c73c2480673d8993b',
                'form': form})
