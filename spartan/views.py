import hashlib

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from forms import SpartanForm
from models import Spartan
from categories.models import Category


@login_required
def spartan(request):
    errors = []
    confirms = []
    if request.method == 'POST':
        if request.user.account.has_related_object():
            return render(request, 'spartan/spartan.html',
                          {'cod': request.user.account.cod,
                           'form': SpartanForm(),
                           'errors': ['You already submitted the form']})
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
            contBancar = hashlib.sha224(contBancar).hexdigest()
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
            print spartan.contBancar
#            spartan.activation_email()
            confirms.append('Ati completat cu succes formularul,'
                            'asteptati confirmarea administratorului!')

        else:
            errors.append('Invalid form')
    form = SpartanForm()
    return render(request, 'spartan/spartan.html', {
        'cod': request.user.account.cod,
        'form': form,
        'confirms': confirms,
        'errors': errors})


@login_required
def user(request, slug):
    curent_spartan = get_object_or_404(Spartan, slug=slug)
    return render(request, 'spartan/SpartanPage.html', {
        'reviews': curent_spartan.reviews,
        'spartan': curent_spartan,
        'img_spartan': curent_spartan.user.account.cod,
        'cod': request.user.account.cod,
    })
