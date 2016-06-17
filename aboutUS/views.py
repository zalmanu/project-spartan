from django.shortcuts import render


def aboutUS(request):
    return render(request, 'aboutUS/aboutUS.html')
