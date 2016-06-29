from django.shortcuts import render
from .models import CreateContact


def contactUS(request):
    confirm = []
    form = CreateContact(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm.append(
                'Your message has been successfully sent!\nThank you!')
    return render(request, 'contactUS/contactUS.html',
                  {'form': form,
                   'confirm': confirm})
