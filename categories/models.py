# Copyright 2015-2016 Emanuel Covaci, Fineas Silaghi, Sebastian Males
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
