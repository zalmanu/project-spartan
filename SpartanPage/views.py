from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required
def user(request):
    performanta= (request.user.spartan.raiting + request.user.spartan.tasks)/2
    return render(request,'SpartanPage/user.html' ,{'performance':performanta,
                                          'reviews':request.user.spartan.reviews})