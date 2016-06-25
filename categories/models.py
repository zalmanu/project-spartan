from __future__ import unicode_literals


from django.db import models


class Category(models.Model):
    name = models.CharField(null=True, max_length=20)
    path_banner = models.CharField(null=True, max_length=500)
    path_bg = models.CharField(null=True, max_length=500)
    path_icon = models.CharField(null=True, max_length=500)
    path_mini = models.CharField(null=True, max_length=500)

    @staticmethod
    def categories():
        categories = []
        for x in Category.objects.all():
            categories.append(x.name)
        return categories
