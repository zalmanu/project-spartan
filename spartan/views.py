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
                          {'cod': request.user.account.code,
                           'form': SpartanForm(),
                           'errors': ['You already submitted the form']})
        form = SpartanForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            birthday = form.cleaned_data['birthday']
            adress = form.cleaned_data['adress']
            cnp = form.cleaned_data['CNP']
            series = form.cleaned_data['series']
            cui = form.cleaned_data['cui']
            bank_account = form.cleaned_data['bank_account']
            if len(bank_account) != 16:
                errors.append("Bank accout has to be 16 digits long")
            bank_account = hashlib.sha224(bank_account).hexdigest()
            category = form.cleaned_data['category']
            category = get_object_or_404(Category, name=category)
            spartan = Spartan.objects.create(last_name=last_name,
                                             first_name=first_name,
                                             birthday=birthday,
                                             address=adress, cnp=cnp,
                                             series=series, cui=cui,
                                             bank_account=bank_account,
                                             category=category,
                                             user=request.user)
            spartan.save()
#            spartan.activation_email()
            confirms.append('Ati completat cu succes formularul,'
                            'asteptati confirmarea administratorului!')

        else:
            errors.append('Invalid form')
    form = SpartanForm()
    return render(request, 'spartan/spartan.html', {
        'cod': request.user.account.code,
        'form': form,
        'confirms': confirms,
        'errors': errors})


@login_required
def user(request, slug):
    curent_spartan = get_object_or_404(Spartan, slug=slug)
    return render(request, 'spartan/SpartanPage.html', {
        'reviews': curent_spartan.reviews,
        'spartan': curent_spartan,
        'img_spartan': curent_spartan.user.account.code,
        'cod': request.user.account.code,
    })
