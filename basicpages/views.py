from django.shortcuts import render


def home(request):
    if request.user.is_authenticated():
        return render(request, 'useractions/home.html')
    else:
        return render(request, 'basicpages/index.html')
