import json

from django.shortcuts import render

from .forms import ReviewForm
import datetime
from .models import Review
from authentication.models import Spartan
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect


@login_required
def review(request, slug):
    errors = []
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if request.POST.get('dontp'):
            return redirect('/')
        if form.is_valid():
            message = form.cleaned_data['message']
            review = Review.objects.create(
                receiver=get_object_or_404(Spartan, slug=slug),
                submitter=request.user,
                message=message, data=datetime.datetime.now()
                )
            review.save()
            curent_spartan = get_object_or_404(Spartan, slug=slug)
            curent_spartan.raiting += 1
            curent_spartan.save()
            return redirect('/')
        else:
            errors.append('Invalid form')

    form = ReviewForm()
    return render(request, 'review/review.html',
                  {'cod': request.user.account.cod,
                   'form': form, 'slug': slug,
                   'errors': errors})
