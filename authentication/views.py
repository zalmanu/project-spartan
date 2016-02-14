from django.shortcuts import render


def register_page(request):
    return render(request, "authentication/register.html")


def login_page(request):
    return render(request, "authentication/logIn.html")
