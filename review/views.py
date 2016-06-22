import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from .forms import ReviewForm
from .models import Review, UrlUnique
from authentication.models import Spartan


@login_required
def review(request, slug, url_hash):
    errors = []
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if request.POST.get('dontp'):
            return redirect('/')
        if form.is_valid():
            url = get_object_or_404(UrlUnique, un_hash=url_hash, expired=False)
            url.expired = True
            url.save()
            message = form.cleaned_data['message']
            review = Review.objects.create(
                receiver=get_object_or_404(Spartan, slug=slug),
                submitter=request.user,
                message=message, data=datetime.datetime.now()
                )
            review.save()
            curent_spartan = get_object_or_404(Spartan, slug=slug)
            curent_spartan.rating += 1
            curent_spartan.save()
            return redirect('/')
        else:
            errors.append('Invalid form')

    form = ReviewForm()
    return render(request, 'review/review.html',
                  {'cod': request.user.account.code,
                   'form': form, 'slug': slug,
                   'errors': errors})
