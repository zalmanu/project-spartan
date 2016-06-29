import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from .models import Review, UrlUnique, CreateReviewForm
from authentication.models import Spartan


@login_required
def review(request, slug, url_hash):
    form = CreateReviewForm(data=request.POST or None)
    if request.method == 'POST':
        if request.POST.get('dontp'):
            return redirect('/')
        if form.is_valid():
            url = get_object_or_404(UrlUnique, un_hash=url_hash, expired=False)
            url.expired = True
            url.save()
            form.instance.receiver = get_object_or_404(Spartan, slug=slug)
            form.instance.submitter = request.user
            form.save()
            curent_spartan = form.instance.receiver
            curent_spartan.rating += 1
            curent_spartan.save()
            return redirect('/')
    return render(request, 'review/review.html',
                  {
                    'cod': request.user.account.code,
                    'form': form, 'slug': slug
                  })
