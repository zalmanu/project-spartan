from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required
def user(request,slug):
    return render(request,'SpartanPage/user.html' ,{
                                          'reviews':request.user.spartan.reviews})