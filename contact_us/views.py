from django.shortcuts import render
from .models import CreateContact
from django.contrib.auth.decorators import login_required


@login_required
def contact_us(request):
    confirm = []
    form = CreateContact(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm.append(
                'Your message has been successfully sent!\nThank you!')
    return render(request, 'contact_us/contact_us.html',
                  {'form': form,
                   'confirm': confirm})
