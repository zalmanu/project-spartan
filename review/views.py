

from django.shortcuts import render

# Create your views here.

from .forms import ReviewForm
import datetime
from .models import Review
from authentication.models import  Spartan
from django.contrib.auth.decorators import login_required

@login_required
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            message= form.cleaned_data['message']

            review=Review.objects.create(receiver=Spartan.objects,submitter=request.user,
                                         message=message,data=datetime.datetime.now()
                                         )
            review.save()
            return render(request, 'useractions/review.html' ,{'errors': ['Multumim pentru review!'],
                                                                'cod': request.user.account.cod,
                                                                 'form':form,
                                                               })
        else:
            return render(request, 'useractions/review.html', {'cod': request.user.account.cod,
                                                                'form': form,
                                                                 'errors':['Invalid form']}
                          )

    else:
         form = ReviewForm()
         if request.user.is_active and not  request.user.is_superuser:
             return render(request, 'useractions/review.html', {'cod': request.user.account.cod,
                                                                        'form': form})
         else :return render(request, 'useractions/review.html', {'cod': 1,
                                                                    'form': form })