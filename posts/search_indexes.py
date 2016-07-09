from haystack import indexes

from .models import Announcement


class AnnouncementIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")
    description = indexes.CharField(model_attr="description")
    slug = indexes.CharField(model_attr="slug")

    def get_model(self):
        return Announcement

    def index_queryset(self, using=Announcement):
        return self.get_model().objects.filter(status=False)
