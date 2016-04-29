from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import ContactUS
from .forms import ContactUSForm


def contactUS(request):
    if request.method == 'POST':
        form = ContactUSForm(request.POST)
        if form.is_valid():
            frist_name = form.cleaned_data['prenume']
            last_name = form.cleaned_data['nume']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            contact = ContactUS.objects.create(frist_name=frist_name,
                                               last_name=last_name,
                                               email=email, phone=phone,
                                               message=message)
            contact.save()
            subject = 'Contact US '
            messagetip = " Buna Admin, \n Ati primit un mesaj " \
                         "de la un utilizator \n" \
                         " Nume : %s ,\n Prenume: %s: \n,Email: %s ," \
                         "\n Phone: %s,\n" \
                         "Message: %s" % (frist_name, last_name,
                                          email, phone, message)
            send_mail(subject, messagetip, email,
                      [settings.EMAIL_HOST_USER], fail_silently=True)
            return render(request, 'contactUS/contactUS.html', {
                'confirm': ['Mesajul a fost trimis cu succes ! \n O zi buna!'],
                'form': form})
        else:
            return render(request, 'contactUS/contactUS.html',
                          {'form': form,
                           'errors': [
                               'Invalid form']
                           })
    else:
        form = ContactUSForm()
        return render(request, 'contactUS/contactUS.html', {'form': form})
