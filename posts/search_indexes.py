from haystack import indexes

from .models import Announcement


class AnnouncementIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(model_attr='title', document=True)
    text = indexes.CharField(model_attr='text')
    author = indexes.CharField(model_attr='author')
    status = indexes.BooleanField(model_attr='status')

    def get_model(self):
        return Announcement

    def index_queryset(self, using=Announcement):
        return self.get_model().objects.filter(status__lte=False)
