from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from models import Category
from useractions.models import Announcement 

@login_required
def category(request, kind):
    categories = Category.objects.all()
    page_category = get_object_or_404(Category, name=kind)
    curruser = request.user
    if request.user.is_active and not request.user.is_superuser:
        return render(request, 'useractions/category.html', {
            'categories': categories,
            'kind': page_category,
            'cod': curruser.account.cod,
            'ann': Announcement.objects.filter(category=page_category, status=False)
        })
    else:
        return render(request, 'useractions/category.html', {
            'categories': categories,
            'kind': page_category,
            'cod': '61e1380365703a4c73c2480673d8993b',
            'ann': Announcement.objects.filter(category=page_category, status=False)
        })

