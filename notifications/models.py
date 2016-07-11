from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    html = models.CharField(max_length=90000, blank=True)
    seen = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='notifications', default="")

    def spartan_notif(self):
        self.html = """
            <span class="photo"><img alt="avatar"
src="http://www.gravatar.com/avatar/""" + self.user.account.code + """></span>
            <span class="subject">
            <span class="from">""" + self.user.username + """</span>
            </span>
            <span class="message">
            A new post <b id="notification-bid">in your area</b>
            </span>
            </a>
            """
