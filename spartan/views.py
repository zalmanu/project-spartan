from django.shortcuts import render,render_to_response
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from forms import SpartanForm
from models import Spartan
from categories.models import Category

@login_required
def spartan(request):
    errors = []
    confirms = []
    if request.method == 'POST':
        if request.user.account.has_related_object():
            return render(request, 'spartan/spartan.html', {'cod': request.user.account.cod,
                                                                'form': SpartanForm(),
                                                                'errors':['You already submitted the form']})
        form = SpartanForm(request.POST)
        if form.is_valid():
            nume = form.cleaned_data['nume']
            prenume = form.cleaned_data['prenume']
            data_nasterii = form.cleaned_data['data']
            adress = form.cleaned_data['adress']
            cnp = form.cleaned_data['CNP']
            serie = form.cleaned_data['serie']
            cui = form.cleaned_data['cui']
            contBancar = form.cleaned_data['cont']
            if len(contBancar) != 16:
                errors.append("Banck accout has to be 16 digits long")
            abilitate = form.cleaned_data['abilitate']
            abilitate = get_object_or_404(Category, name=abilitate)
            spartan = Spartan.objects.create(nume=nume, prenume=prenume,
                                             data_nasterii=data_nasterii,
                                             address=adress, cnp=cnp,
                                             serie=serie, cui=cui,
                                             contBancar=contBancar,
                                             abilitate=abilitate,
                                             user=request.user)
            spartan.save()
            subject = 'Activare putere de Spartan'
            messagetip = " Buna % s , \n Ati completat formularul" \
                         " pentru activare puterii de Spartan \n" \
                         " Nume : %s ,\n Prenume: %s \n Data nasterii: %s \n" \
                         " Adresa : %s \n CNP: %s \n Serie: %s \n" \
                         " CUI : %s \n Cont Bancar: %s \n " \
                         "Abilitate 1: %s \n  Datele dvs. vor fi analizate " \
                         "de Admin in vederea" \
                         " Activarii Puterii de Spartan \nO zi buna!" % (
                             request.user.username, nume, prenume,
                             data_nasterii,
                             adress, cnp, serie, cui, contBancar, abilitate)
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, messagetip, from_email,
                      [request.user.email], fail_silently=True)
            confirms.append('Ati completat cu succes formularul, asteptati confirmarea administratorului!')

        else:
            errors.append('Invalid form')
    form = SpartanForm()
    return render(request, 'spartan/spartan.html',{
        'cod': request.user.account.cod,
        'form': form, 
        'confirms':confirms,
        'errors': errors })


@login_required
def user(request,slug):
    curent_spartan = get_object_or_404(Spartan, slug=slug)
    return render(request,'spartan/SpartanPage.html' ,{
                                          'reviews': curent_spartan.reviews,
                                           'spartan':curent_spartan,
                                            'img_spartan':curent_spartan.user.account.cod,
                                            'cod':request.user.account.cod,
    })


