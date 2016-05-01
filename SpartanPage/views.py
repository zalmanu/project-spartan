from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from authentication.models import Spartan
# Create your views here.
@login_required
def user(request,slug):
    curent_spartan = get_object_or_404(Spartan, slug=slug)
    return render(request,'SpartanPage/user.html' ,{
                                          'reviews':request.user.spartan.reviews,
                                           'spartan':curent_spartan,
                                            'img_spartan':curent_spartan.user.account.cod,
                                            'cod':request.user.account.cod,
    })