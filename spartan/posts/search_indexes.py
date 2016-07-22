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
