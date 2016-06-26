from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import ContactUS
from .forms import ContactUSForm


def contactUS(request):
    confirm = []
    errors = []
    form = ContactUSForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            contact = ContactUS.objects.create(first_name=first_name,
                                               last_name=last_name,
                                               email=email, phone=phone,
                                               message=message)
            contact.save()
            subject = 'Contact US '
            messagetip = " Buna Admin, \n Ati primit un mesaj " \
                         "de la un utilizator \n" \
                         " Last_Name : %s ,\n Nume: %s: \n,Email: %s ," \
                         "\n Phone: %s,\n" \
                         "Message: %s" % (first_name, last_name,
                                          email, phone, message)
            send_mail(subject, messagetip, email,
                      [settings.EMAIL_HOST_USER], fail_silently=True)
            confirm.append(
                'Your message has been successfully sent!\nThank you!')
        else:
            errors.append('Invalid form')
    return render(request, 'contactUS/contactUS.html',
                  {'form': form,
                   'errors': errors,
                   'confirm': confirm})
