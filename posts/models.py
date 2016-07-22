# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from spartans.models import Spartan
from categories.models import Category


def upload_location(instance, filename):
    return "%s/%s" % (instance.slug, filename)


class Announcement(models.Model):
    title = models.CharField(null=True, max_length=256)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              height_field="height_field",
                              width_field="width_field")
    image2 = models.ImageField(upload_to=upload_location,
                               null=True, blank=True,
                               height_field="height_field",
                               width_field="width_field")
    image3 = models.ImageField(upload_to=upload_location,
                               null=True, blank=True,
                               height_field="height_field",
                               width_field="width_field")
    image4 = models.ImageField(upload_to=upload_location,
                               null=True, blank=True,
                               height_field="height_field",
                               width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    description = models.CharField('Announcement description',
                                   null=True, max_length=500)
    slug = models.SlugField(default=uuid.uuid1, unique=True)
    author = models.ForeignKey(to=User, related_name='posts',
                               null=True, blank=True)
    address = models.CharField(null=True, max_length=500)
    country = models.TextField(null=True, max_length=50)
    city = models.TextField(null=True, max_length=100)
    data = models.DateField('Date FORMAT YYYY-MM-DD',
                            null=True)
    creation_date = models.DateTimeField(editable=False, auto_now_add=True,
                                         null=True)
    timePost = models.TimeField('Time FORMAT HH:MM:SS', null=True)
    category = models.ForeignKey(Category, null=True)
    money = models.IntegerField('Highest price you are willing to pay (EUR)',
                                null=True)
    spartan = models.ForeignKey(Spartan, related_name='anunturi', null=True,
                                blank=True)
    price = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)
    employer_done = models.BooleanField(default=False)
    spartan_done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=[self.slug])

    def edit_url(self):
        return reverse('post', args=[self.slug])

    class Meta:
        get_latest_by = 'creation_date'
