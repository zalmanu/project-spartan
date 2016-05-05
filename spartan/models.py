from __future__ import unicode_literals
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from categories.models import Category
from django.core.urlresolvers import reverse

class Spartan(models.Model):
    nume = models.CharField(max_length=40)
    prenume = models.CharField(max_length=40)
    data_nasterii = models.DateField('Data nasterii', null=True)
    address = models.CharField(null=True, max_length=500)
    cnp = models.IntegerField(null=True)
    serie = models.CharField(max_length=30, null=True)
    cui = models.CharField(max_length=30, null=True)
    contBancar = models.CharField(max_length=30, null=True)
    abilitate = models.ForeignKey(Category, null=True)
    user = models.OneToOneField(User, primary_key=True, default='')
    spartanStatus = models.BooleanField(default=False)
    raiting = models.IntegerField(default=0)
    tasks = models.IntegerField(default=0)
    slug = models.SlugField(default=uuid.uuid1, unique=True)

    def get_absolute_url(self):
        return reverse('users', args=[self.slug])
        
    def activation_email(self):
        subject = 'Spartan activation'
        messagetip = " Hi! % s , \n You submitted the form" \
                     " for becoming a spartan!\n" \
                     " Last name : %s ,\n First name : %s \n Birthday: %s \n" \
                     " Adresa : %s \n CNP: %s \n Serie: %s \n" \
                     " CUI : %s \n Bank account: %s \n " \
                     "Ability: %s \n  An admin will respond soon. " \
                     " - Team Spartan" % (
                         self.user.username, self.nume, self.prenume,
                         self.data_nasterii, self.address, self.cnp, 
                         self.serie, self.cui, self.contBancar, self.abilitate.name)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, messagetip, from_email,
                  [self.user.email], fail_silently=True)
