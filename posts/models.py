from __future__ import unicode_literals
import uuid

from django.db import models

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


from django.core.urlresolvers import reverse
from spartans.models import Spartan
from categories.models import Category


class Announcement(models.Model):
    title = models.CharField(null=True, max_length=256)
    text = models.CharField('Announcement description',
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

    def get_absolute_url(self):
        return reverse('post', args=[self.slug])

    def edit_url(self):
        return reverse('post', args=[self.slug])

    def creation_email(self, user):
        subject = 'Anunt Project Spartan'
        messagetip = " Hi! % s , \n You successfully posted an announce! \n" \
                     " Title: %s ,\n Description: %s \n Address: %s \n " \
                     "Country : %s \n City: %s \n Category: %s \n" \
                     " Time : %s \n Date: %s \n " \
                     "Highest bid price: %s eur \n" \
                     " Have a nice day! - Team Spartan" % (
                         user.username, self.title,  self.text,  self.address,
                         self.country,  self.city,  self.category.name,
                         self.timePost, self.data, self.money)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, messagetip, from_email,
                  [user.email], fail_silently=True)

    class Meta:
        get_latest_by = 'creation_date'

