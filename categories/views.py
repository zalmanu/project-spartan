from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from models import Category
from posts.models import Announcement


@login_required
def category(request, kind):
    categories = Category.objects.all()
    page_category = get_object_or_404(Category, name=kind)
    curruser = request.user
    return render(request, 'category/category.html', {
        'categories': categories,
        'kind': page_category,
        'cod': curruser.account.code,
        'ann': Announcement.objects.filter(category=page_category,
                                           status=False)
    })
