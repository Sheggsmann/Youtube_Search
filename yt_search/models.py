from django.db import models
from django.conf import settings



class Contact(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True)
    video_id = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=100)
    channel_name = models.CharField(max_length=100)
    date_contacted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_id
