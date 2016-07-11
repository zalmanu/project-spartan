import json

from background_task import background
from channels import Group

from spartans.models import Spartan
from notifications.models import Notification
from categories.models import Category


@background(schedule=5)
def notif_spartans(city, categoryname):
    category = Category.objects.get(name=categoryname)
    for spartan in Spartan.objects.filter(spartanStatus=True,
                                          category=category):
        notification = Notification.objects.create(receiver=spartan.user)
        notification.spartan_notif()
        notification.save()
        dic = {
            'author': notification.user.username,
            'html': notification.html
        }
        Group("spartans-" + category + "-" + city).send(
            {'text': json.dumps(dic)})
