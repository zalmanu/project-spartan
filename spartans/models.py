from __future__ import unicode_literals

import uuid

from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from django.core.urlresolvers import reverse

from categories.models import Category


class Spartan(models.Model):
    last_name = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    birthday = models.DateField('Date FORMAT YYYY-MM-DD', null=True)
    address = models.CharField(null=True, max_length=500)
    cnp = models.CharField('CNP', null=True, max_length=20)
    series = models.CharField('ID card series', max_length=30, null=True)
    cui = models.CharField('CUI', max_length=30, null=True)
    bank = models.CharField('Bank account', max_length=60,
                            null=True)
    category = models.ForeignKey(Category, null=True)
    user = models.OneToOneField(User, primary_key=True, default='')
    spartanStatus = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    tasks = models.IntegerField(default=0)
    slug = models.SlugField(default=uuid.uuid1, unique=True)

    def get_absolute_url(self):
        return reverse('users', args=[self.slug])

    def activation_email(self):
        subject = 'Spartan activation'
        email = " Hi! % s , \n You submitted the form" \
                " for becoming a spartan!\n" \
                " Last name : %s ,\n First name : %s \n Birthday: %s \n" \
                " Address : %s \n CNP: %s \n Serie: %s \n" \
                " CUI : %s \n Bank account: %s \n " \
                "Ability: %s \n  An admin will respond soon. " \
                " - Team Spartan" % (
                         self.user.username, self.last_name, self.first_name,
                         self.birthday, self.address,
                         self.cnp, self.series, self.cui,
                         self.bank, self.category.name)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, email, from_email,
                  [self.user.email], fail_silently=True)
