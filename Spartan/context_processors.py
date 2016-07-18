from posts.models import Announcement
from categories.models import Category


def template_context(request):
    return {
        'ann': Announcement.objects.filter(status=False).order_by(
            'creation_date')[:8],
        'user': request.user,
        'categories': Category.objects.all()
    }
