from django.shortcuts import render


def faq(request):
    return render(request, 'faq/faq.html')
