from haystack import indexes

from .models import Announcement


class AnnouncementIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")
    author = indexes.CharField(model_attr='author')
    status = indexes.BooleanField(model_attr='status')

    def get_model(self):
        return Announcement

    def index_queryset(self, using=Announcement):
        return self.get_model().objects.filter(status=False)
